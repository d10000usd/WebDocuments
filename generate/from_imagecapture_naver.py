import os,sys
import random

from pytube import YouTube
import cv2
import dlib
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from from_MODULE import ColorPrinter as cp
from from_MODULE import FileReader as fr
# from from_MODULE import ColorPrinter as cp

CurrentPath = "/Users/hg/PROJECT/frontend/hg-project-bootstrap/src/assets/coinInfo"
class VideoDownloader:
    def __init__(self, url, save_path):
        self.url = url
        self.save_path = save_path

    def download_video(self):
        youtube = YouTube(self.url)
        all_streams = youtube.streams
        filtered_streams = all_streams.filter(res="1080p")
        
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)
        video = filtered_streams.first()
        video.download(self.save_path)
        return self.save_path, video.default_filename

class VideoProcessor:
    def __init__(self, url, save_folder,secperInterval):
        self.url = url
        self.save_folder = save_folder
        self.seconds_per_interval = secperInterval 
        self.save_path = f"/Users/hg/PROJECT/acloud/public/img/{self.save_folder}"
        self.face_detector = ImageProcessing()
        self.video_downloader = VideoDownloader(self.url, self.save_path)

    def process_video(self, video_path, filename,addtext,seodict,imageFolder):
        cap = cv2.VideoCapture(video_path + "/" + filename)
        frame_rate = cap.get(cv2.CAP_PROP_FPS)
        
        interval_frames = int(frame_rate * self.seconds_per_interval)
        frame_count = 0
        idx = 0
        iterator = iter(seodict.items())    
        imagedict = {}
        while True:
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_count)
            success, image = cap.read()
            if not success:
                break
            
            key, value = next(iterator)
            addtext["imgDict"]['text'] = key
            addtext["imgDict1"]['text'] = value
            facePos = self.face_detector.detect_faces(image)
            image=self.face_detector.add_image_circle_line( image, addtext["deco_line"])
            image=self.face_detector.add_text_to_image_center( image, addtext["imgDict"])
            image=self.face_detector.add_text_to_image_center( image, addtext["imgDict1"])
            if len(facePos) == 0:
                
                imagedict[f"path{idx}"] = f'{imageFolder}/frame_at_{int(round(frame_count/frame_rate,0))}_seconds.jpg'
                self.savaImage(image, frame_count, frame_rate, imageFolder)
            frame_count += interval_frames

            # cv2.imshow('frame', image)
            # key = cv2.waitKey(1)
            # if key == 27:
            #     break
            idx =idx+1
        fr.save_json("/Users/hg/DEV/WebDocuments/public/img/th/image.json",imagedict)
        cap.release()

    def savaImage(self, image, frame_count, frame_rate, imageFolder):
        cv2.imwrite(f'{imageFolder}/frame_at_{int(round(frame_count/frame_rate,0))}_seconds.jpg', image)  # 이미지 저장
        cp.prLightPurple(f'{imageFolder}/frame_at_{int(round(frame_count/frame_rate,0))}_seconds.jpg')
        # Do something with the faces if needed

class ImageProcessing:
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()
        self.imageSave="/Users/hg/DEV/WebDocuments/public/img/th"
        self.sourceFilePath = "/Users/hg/DEV/WebDocuments/public/img/flower"
        self.sourceFileName = "lol.mp4"
    def detect_faces(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.detector(gray)

        return faces

    def add_text_to_image_center(self, image, imgDict):
        text = imgDict["text"]
        font_size = imgDict["font_size"]
        text_color = imgDict["text_color"]
        bg_alpha_value = imgDict["bg_alpha_value"]
        fontpath = imgDict["fontpath"]
        topmargin = imgDict["topmargin"]
     

        # Load image
        img_pil = Image.fromarray(image)
        draw = ImageDraw.Draw(img_pil)


        # Set font
        try:
            font = ImageFont.truetype(fontpath, font_size)
        except IOError:
            print("Font file not found")
            return image

        # Get text size
        textbbox = draw.textbbox((0, 0), text, font=font)
        text_width = textbbox[2] - textbbox[0]
        text_height = textbbox[3] - textbbox[1]

        # Calculate text position 가운데서 y축 위로 옴겨서 적용
        x = (image.shape[1] - text_width) / 2 
        y = (image.shape[0] - text_height) / 2 -130 + topmargin

        # Draw text on image with transparency
        text_img = Image.new('RGBA', (image.shape[1], image.shape[0]), (255, 255, 255, bg_alpha_value))
        text_draw = ImageDraw.Draw(text_img)
        text_draw.text((x, y), "" + text, font=font, fill=text_color)

        # Combine image and text with transparency
        result = Image.alpha_composite(img_pil.convert('RGBA'), text_img)

        # Convert back to OpenCV format
        image_with_text = np.array(result.convert('RGB'))

        return image_with_text

    def add_image_circle_line(self, image, imgDict):
        random_number = random.randint(1, 200)
        random_number1 = random.randint(1, 200)
        random_number2 = random.randint(499, 2200)
        random_number3 = random.randint(499, 2200)
        linepos = [(random_number, random_number1), (random_number2, random_number3)]
        # ellipsepos = imgDict['circle_pos']

        # Convert the image to the BGR format
        image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Create a transparent overlay image
        overlay = image.copy()

        # Draw a semi-transparent line on the overlay
        cv2.line(overlay, linepos[0], linepos[1], imgDict["linecolor"], imgDict["linewidth"])

        # Combine the original image and the overlay with transparency
        added_image = cv2.addWeighted(image_bgr, 0.7, overlay, 0.3, 0)

        # Convert the image back to RGB format
        image_with_text = cv2.cvtColor(added_image, cv2.COLOR_BGR2RGB)

        return image_with_text

    def add_image_circle_line_ct(self, image, imgDict):
        random_number = random.randint(1, 200) 
        random_number1 = random.randint(1, 200) 
        random_number2 = random.randint(499, 2200) 
        random_number3 = random.randint(499, 2200) 
        linepos=[(random_number, random_number1), (random_number2, random_number3)]
        ellipsepos = imgDict['circle_pos']
        # linepos = imgDict['line_pos']
        # Load image
        img_pil = Image.fromarray(image)
        draw = ImageDraw.Draw(img_pil)

        draw.line(linepos, fill=imgDict["linecolor"], width=imgDict["linewidth"])
        
        draw.ellipse(ellipsepos, fill=imgDict["circlecolor"])

        image_with_text = np.array(img_pil)

        return image_with_text
    def thumnailMain(self,imageFolder,ticker):
        cp.LOGMODULE(f"{sys._getframe().f_code.co_name} {ticker}") 
        # seo_dict1 = {
        #                 "키워드 연구": "인기 검색어 및 검색 트렌드를 분석하여 적합한 키워드를 식별합니다.",
        #                 "메타 태그 최적화": "웹 페이지의 메타 데이터를 최적화하여 검색 엔진에 적합한 정보를 제공합니다.",
        #                 "콘텐츠 최적화": "웹사이트 콘텐츠를 최적화하여 검색 엔진에서 높은 순위를 달성할 수 있습니다.",
        #                 "백링크 구축": "다른 웹사이트로부터의 백링크를 구축하여 검색 엔진의 신뢰도를 향상시킵니다.",
        #                 "검색 엔진 색인": "웹 페이지를 검색 엔진에 색인하여 사용자 검색 결과에 표시되도록 합니다.",
        #                 "사이트 속도 최적화": "웹 사이트의 로딩 속도를 최적화하여 사용자 경험을 향상시킵니다.",
        #                 "모바일 친화적 웹사이트": "모바일 기기에서 웹 사이트가 원활하게 표시되도록 합니다.",
        #                 "사이트 구조 최적화": "웹 사이트의 구조를 최적화하여 검색 엔진이 콘텐츠를 쉽게 이해할 수 있도록 합니다.",
        #                 "로컬 SEO": "지역 사업체의 온라인 가시성을 향상시키기 위한 SEO 전략을 구현합니다.",
        #                 "이미지 최적화": "이미지 파일의 크기와 형식을 최적화하여 웹 페이지 로딩 속도를 향상시킵니다.",
        #                 "품질 콘텐츠 제공": "유용하고 유익한 콘텐츠를 제공하여 사용자의 관심을 유발합니다.",
        #                 "검색 엔진 크롤링 가능성": "검색 엔진이 웹 사이트를 쉽게 크롤링할 수 있도록 합니다.",
        #                 "소셜 미디어 통합": "소셜 미디어 플랫폼을 활용하여 온라인 커뮤니티와 상호 작용합니다.",
        #                 "링크 구조 최적화": "내부 및 외부 링크를 최적화하여 검색 엔진의 신뢰도를 향상시킵니다.",
        #                 "경쟁 분석": "경쟁사의 온라인 전략을 분석하여 자사의 전략을 개선합니다.",
        #                 "사용자 경험 개선": "웹 사이트의 사용자 경험을 향상시켜 재방문률을 높입니다.",
        #                 "검색 엔진 알고리즘 업데이트": "주요 검색 엔진의 알고리즘 변화에 대응하여 전략을 수정합니다.",
        #                 "키워드 밀도 관리": "키워드의 적절한 빈도로 사용하여 검색 엔진에 적합한 콘텐츠를 제공합니다.",
        #                 "링크 건강 관리": "링크 프로필을 관리하여 불량 링크로부터 웹 사이트를 보호합니다.",
        #                 "SEO 성과 측정": "SEO 노력의 성과를 측정하여 전략의 효과를 평가합니다."
        #       }
        seo_dict1 = {
                f"{ticker}": f"{ticker} 검색어 및 검색 트렌드를 분석하여\n  적합한 키워드를 식별합니다.",
                "메타 태그\n 최적화": "웹 페이지의 메타 데이터를\n  최적화하여 검색 엔진에\n  적합한 정보를 제공합니다.",
                "콘텐츠 최적화": "웹사이트 콘텐츠를 최적화하여\n 검색 엔진에서\n 높은 순위를 달성할 수 있습니다.",
                "백링크 구축": "다른 웹사이트로부터의 백링크를 구축하여 \n검색 엔진의 신뢰도를 향상시킵니다.",
                "검색 엔진 색인": "웹 페이지를 검색 엔진에 색인하여\n 사용자 검색 결과에 표시되도록 합니다.",
                "사이트 속도\n 최적화": "웹 사이트의 로딩 속도를\n 최적화하여 사용자\n 경험을 향상시킵니다.",
                "모바일 친화적\n 웹사이트": "모바일 기기에서 웹 사이트가\n 원활하게 표시되도록 합니다.",
                "사이트 구조\n 최적화": "웹 사이트의 구조를 최적화하여\n 검색 엔진이 콘텐츠를 쉽게 이해할 수 있도록 합니다.",
                "로컬 SEO": "지역 사업체의 온라인 가시성을\n 향상시키기 위한 SEO 전략을 구현합니다.",
                "이미지 최적화": "이미지 파일의 크기와 형식을\n 최적화하여 웹 페이지 로딩 속도를 향상시킵니다.",
                "품질 콘텐츠 제공": "유용하고 유익한 콘텐츠를\n 제공하여 사용자의 관심을 유발합니다.",
                "검색 엔진\n 크롤링 가능성": "검색 엔진이 웹 \n사이트를 쉽게 크롤링할 수 있도록 합니다.",
                "소셜 미디어 통합": "소셜 미디어 플랫폼을 활용하여\n 온라인 커뮤니티와 상호 작용합니다.",
                "링크 구조 최적화": "내부 및 외부 링크를 최적화하여\n 검색 엔진의 신뢰도를 향상시킵니다.",
                "경쟁 분석": "경쟁사의 온라인 전략을 분석하여\n 자사의 전략을 개선합니다.",
                "사용자 경험 개선": "웹 사이트의 사용자 경험을\n 향상시켜 재방문률을 높입니다.",
                "검색 엔진\n알고리즘 업데이트": "주요 검색 엔진의 알고리즘\n 변화에 대응하여 전략을 수정합니다.",
                "키워드 밀도 관리": "키워드의 적절한 빈도로 사용하여\n 검색 엔진에 적합한 콘텐츠를 제공합니다.",
                "링크 건강 관리": "링크 프로필을 관리하여 불량\n 링크로부터 웹 사이트를 보호합니다.",
                "SEO 성과 측정": "SEO 노력의 성과를 측정하여\n 전략의 효과를 평가합니다."
            }

        seo_dict = {
                f"{ticker}": f"{ticker}",
                f"{ticker}": f"{ticker}",
                f"{ticker}": f"{ticker}",
                f"{ticker}": f"{ticker}",
            }
        
        config = {
                'imgDict' : {
                    "text": "Deep\n\n(RGB value)opacity",
                    "font_size": 150,  # 폰트 크기
                    "text_color": (255, 255, 255, 255),  # 텍스트 색상 (RGB 값)투명도
                    "text_alignment": "center",  # 텍스트 정렬 ("center", "left", "right" 중 하나 선택)
                    "bg_alpha_value":1,
                    "fontpath" :"/Users/hg/DEV/WebDocuments/public/font/MaruBuri-SemiBold.ttf",
                    "topmargin" : 0,
            
                },
                "imgDict1" : {
                    "text": "payloads and bypasses for Web ",
                    "font_size": 55,  # 폰트 크기
                    "text_color": (163, 204, 255,255),  # 텍스트 색상 (RGB 값)
                    "text_alignment": "center",  # 텍스트 정렬 ("center", "left", "right" 중 하나 선택)]
                    "bg_alpha_value":45,
                    "fontpath" :"/Users/hg/DEV/WebDocuments/public/font/MaruBuri-Bold.ttf",
                    "topmargin" : 330,
                
                },
                "deco_line": {"linecolor" : (60, 204, 255, 255),
                            "linewidth" :1213,
                            "circlecolor" : (102, 255, 51, 255),
                            "circle_pos" : [(90, 90), (600, 600)],
                            "line_pos" :[(0, 120), (120, 0)]

                            }
            }
    
        url1 = 'https://www.youtube.com/watch?v=uwmDH12MAA4&ab_channel=MarvelEntertainment'
        

        secondsPerInterval = 60 # 60 이 1분
        video_processor = VideoProcessor(url1, self.sourceFilePath,secondsPerInterval)
        # videopath, file_name = video_processor.video_downloader.download_video()

        
        
        video_processor.process_video(self.sourceFilePath, self.sourceFileName,config,seo_dict,imageFolder)
ImageProcessing().thumnailMain("/Users/hg/DEV/WebDocuments/public/img/th","websocket")
