import os
import xml.etree.ElementTree as ET

def data_processing(folder_path):
    file_list = os.listdir(folder_path)
    
    file_list.sort()
    
    images = []
    xmls = []
    for file in file_list:
        if "jpg" in file:
            images.append(folder_path+"/"+file)
        if "xml" in file:
            xmls.append(folder_path+"/"+file)
    return {
        "images":images,
        "xml":xmls
    }

def extract_xml(xml_file_path):
    tree = ET.parse(xml_file_path)
    #print(tree)
    root = tree.getroot()

    list_with_all_boxes = []
    list_with_all_label = []
    #list_with_image = []
    for boxes in root.iter('object'):

        #filename = root.find('filename').text

        ymin, xmin, ymax, xmax = None, None, None, None

        ymin = int(float(boxes.find("bndbox/ymin").text))
        xmin = int(float(boxes.find("bndbox/xmin").text))
        ymax = int(float(boxes.find("bndbox/ymax").text))
        xmax = int(float(boxes.find("bndbox/xmax").text))
        label = boxes.find("name").text
        list_with_single_boxes = [xmin, ymin, xmax, ymax]
        list_with_all_boxes.append(list_with_single_boxes)
        list_with_all_label.append(label)
        # if (len(label) == 0):
        #     print(xml_file_path)
    return list_with_all_boxes,list_with_all_label