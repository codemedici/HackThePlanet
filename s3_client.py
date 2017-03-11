#!/usr/bin/env python3

import sys
import requests
import requests_aws4auth
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import mimetypes
import argparse

access_id = '' # INSERT YOUR ACCESS ID!
access_key = '' # INSERT YOUR ACCESS KEY!
region = 'eu-west-2' # London
endpoint = 's3-{}.amazonaws.com'.format(region)
auth = requests_aws4auth.AWS4Auth(access_id, access_key, region, 's3')
ns = 'http://s3.amazonaws.com/doc/2006-03-01/'

def xml_pprint(xml_string):
    print(minidom.parseString(xml_string).toprettyxml())

def create_bucket(bucket):
    XML = ET.Element('CreateBucketConfiguration')
    XML.attrib['xmlns'] = ns
    location = ET.SubElement(XML, 'LocationConstraint')
    location.text = auth.region
    data = ET.tostring(XML, encoding='utf-8')
    url = 'http://{}.{}'.format(bucket, endpoint)
    r = requests.put(url, data=data, auth=auth)
    if r.ok:
        print('Created bucket {} OK'.format(bucket))
    else:
        handle_error(r)

def upload_file(bucket, s3_name, local_path, acl='private'):
    data = open(local_path, 'rb').read()
    url = 'http://{}.{}/{}'.format(bucket, endpoint, s3_name)
    headers = {'x-amz-acl': acl}
    mimetype = mimetypes.guess_type(local_path)[0]
    if mimetype:
        headers['Content-Type'] = mimetype
    r = requests.put(url, data=data, headers=headers, auth=auth)
    if r.ok:
        print('Uploaded {} OK'.format(local_path))
    else:
        handle_error(r)

def download_file(bucket, s3_name, local_path):
    url = 'http://{}.{}/{}'.format(bucket, endpoint, s3_name)
    r = requests.get(url, auth=auth)
    if r.ok:
        open(local_path, 'wb').write(r.content)
        print('Downloaded {} OK'.format(s3_name))
    else:
        handle_error(r)

def handle_error(response):
    output = 'Status code: {}\n'.format(response.status_code)
    root = ET.fromstring(response.text)
    code =  root.find('Code').text
    output += 'Error code: {}\n'.format(code)
    message = root.find('Message').text
    output += 'Message: {}\n'.format(message)
    print(output)

def list_buckets():
    """ Lists buckets owned by us """
    url = 'http://{}'.format(endpoint)
    r = requests.get(url, auth=auth)
    if not r.ok:
        handle_error(r)
        return
    # Remove XML namespace declaration before we parse to XML. Doing this
    # because there isn't a neat way of handling namespaces with ElementTree.
    # Although something of a hack this works in practice here because we only
    # have a single namespace declared.
    xml_text = r.text.replace('xmlns="{}"'.format(ns), '')
    root = ET.fromstring(xml_text)
    # root.iter() works like root.findall() except that it searches all
    # descendents of the node, not just the immediate children.
    for element in root.iter('Name'):
        print(element.text)

def list_bucket(bucket):
    """ List the objects in a bucket """
    url = 'http://{}.{}'.format(bucket, endpoint)
    r = requests.get(url, auth=auth)
    if not r.ok:
        handle_error(r)
        return
    # Again removing XML namespace declaration as in list_buckets()
    xml_text = r.text.replace('xmlns="{}"'.format(ns), '')
    root = ET.fromstring(xml_text)
    # root.iter() works like root.findall() except that it searches all
    # descendents of the node, not just the immediate children.
    for element in root.iter('Key'):
        print(element.text)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("create_bucket")

    args = parser.parse_args()

    if len(sys.argv) < 3:
        print(args.create_bucket)
        sys.exit(1)
    else:
        cmd, *args = sys.argv[1:]
        globals()[cmd](*args)


