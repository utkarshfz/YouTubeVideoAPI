# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from video import Video


class VideoDetailList:
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, video_list: List[Video]=None):  # noqa: E501
        """VideoDetailList - a model defined in Swagger

        :param video_list: The video_list of this VideoDetailList.  # noqa: E501
        :type video_list: List[Video]
        """
        self.swagger_types = {
            'video_list': List[Video]
        }

        self.attribute_map = {
            'video_list': 'videoList'
        }
        self._video_list = video_list


    @property
    def video_list(self) -> List[Video]:
        """Gets the video_list of this VideoDetailList.


        :return: The video_list of this VideoDetailList.
        :rtype: List[Video]
        """
        return self._video_list

    @video_list.setter
    def video_list(self, video_list: List[Video]):
        """Sets the video_list of this VideoDetailList.


        :param video_list: The video_list of this VideoDetailList.
        :type video_list: List[Video]
        """
        if video_list is None:
            raise ValueError("Invalid value for `video_list`, must not be `None`")  # noqa: E501

        self._video_list = video_list
