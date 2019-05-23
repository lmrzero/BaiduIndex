import pytesseract
from PIL import Image
import  cv2
import aircv as ac
path = "../baidu/"
# image = Image.open(str(path) + "zoom.jpg")
#
# code = pytesseract.image_to_string(image)
# print code
# print circle_center_pos
def draw_circle(img, p1, p2, color, line_width):
    #cv2.circle(img, pos, circle_radius, color, line_width)
    cv2.rectangle(img, p1, p2, color, line_width)
    cv2.imshow('objDetect', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    im = cv2.imread(path+"3.png")
    obj = cv2.imread(path+"obj.png")
    pos = ac.find_template(im,obj)
    ran = pos["rectangle"]
    objrex = ran[2][0] - ran[0][0]
    objrey = ran[1][1] - ran[0][1]
    re = im[ran[0][1]+int(1.0/2.0*objrey):ran[3][1],ran[0][0]+int(1.0/4.0*objrex):ran[3][0]-int(1.0/2.0*objrex)]
    cv2.imwrite('./aa.png',re)
    ima = cv2.imread('./aa.png')
    yx = ima.shape[1]
    yy = ima.shape[0]
    res = cv2.resize(ima,(yx*2,yy*2),interpolation=cv2.INTER_CUBIC)
    cv2.imwrite('./aa1.png',res)
    image = Image.open('./aa1.png')
    #
    code = pytesseract.image_to_string(image)
    print code
    # circle_center_pos = pos['result']
    # circle_radius = 50
    # color = (0, 255, 0)
    # line_width = 2
    # draw_circle(im, ran[0], ran[3], color, line_width)

