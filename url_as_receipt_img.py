#!/usr/bin/env python3
import subprocess


def fetch_screenshot(url, img):
    """Fetch a screenshot at url, store it at path img"""
    subprocess.run(['google-chrome', '--headless', '--disable-gpu',
                    '--window-size=384,5000', '--hide-scrollbars',
                    '--screenshot={}'.format(img), url])


def trim_bottom(img):
    """Trims the bottom of an image file at path img"""
    subprocess.run(['mogrify',
                    '-background', 'blue',
                    '-splice', '0x1',
                    '-background', 'red',
                    '-splice', '0x1',
                    '-trim',
                    '+repage',
                    '-chop', '0x1', img])


def main():
    img = 'screenshot_test.png'
    fetch_screenshot('https://m.xkcd.com/', 'screenshot_test.png')
    trim_bottom(img)


if __name__ == '__main__':
    main()
