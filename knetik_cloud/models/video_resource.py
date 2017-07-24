# coding: utf-8

"""
    Knetik Platform API Documentation latest 

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://knetikcloud.com.

    OpenAPI spec version: latest 
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VideoResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'active': 'bool',
        'author': 'SimpleReferenceResourcelong',
        'authored': 'int',
        'banned': 'bool',
        'category': 'SimpleReferenceResourcestring',
        'comments': 'list[CommentResource]',
        'contributors': 'list[ContributionResource]',
        'created_date': 'int',
        'embed': 'str',
        'extension': 'str',
        'height': 'int',
        'id': 'int',
        'length': 'int',
        'location': 'str',
        'long_description': 'str',
        'mime_type': 'str',
        'name': 'str',
        'priority': 'int',
        'privacy': 'str',
        'published': 'bool',
        'short_description': 'str',
        'size': 'int',
        'tags': 'list[str]',
        'thumbnail': 'str',
        'updated_date': 'int',
        'uploader': 'SimpleUserResource',
        'views': 'int',
        'width': 'int'
    }

    attribute_map = {
        'active': 'active',
        'author': 'author',
        'authored': 'authored',
        'banned': 'banned',
        'category': 'category',
        'comments': 'comments',
        'contributors': 'contributors',
        'created_date': 'created_date',
        'embed': 'embed',
        'extension': 'extension',
        'height': 'height',
        'id': 'id',
        'length': 'length',
        'location': 'location',
        'long_description': 'long_description',
        'mime_type': 'mime_type',
        'name': 'name',
        'priority': 'priority',
        'privacy': 'privacy',
        'published': 'published',
        'short_description': 'short_description',
        'size': 'size',
        'tags': 'tags',
        'thumbnail': 'thumbnail',
        'updated_date': 'updated_date',
        'uploader': 'uploader',
        'views': 'views',
        'width': 'width'
    }

    def __init__(self, active=None, author=None, authored=None, banned=None, category=None, comments=None, contributors=None, created_date=None, embed=None, extension=None, height=None, id=None, length=None, location=None, long_description=None, mime_type=None, name=None, priority=None, privacy=None, published=None, short_description=None, size=None, tags=None, thumbnail=None, updated_date=None, uploader=None, views=None, width=None):
        """
        VideoResource - a model defined in Swagger
        """

        self._active = None
        self._author = None
        self._authored = None
        self._banned = None
        self._category = None
        self._comments = None
        self._contributors = None
        self._created_date = None
        self._embed = None
        self._extension = None
        self._height = None
        self._id = None
        self._length = None
        self._location = None
        self._long_description = None
        self._mime_type = None
        self._name = None
        self._priority = None
        self._privacy = None
        self._published = None
        self._short_description = None
        self._size = None
        self._tags = None
        self._thumbnail = None
        self._updated_date = None
        self._uploader = None
        self._views = None
        self._width = None

        if active is not None:
          self.active = active
        if author is not None:
          self.author = author
        if authored is not None:
          self.authored = authored
        if banned is not None:
          self.banned = banned
        self.category = category
        if comments is not None:
          self.comments = comments
        if contributors is not None:
          self.contributors = contributors
        if created_date is not None:
          self.created_date = created_date
        if embed is not None:
          self.embed = embed
        self.extension = extension
        self.height = height
        if id is not None:
          self.id = id
        self.length = length
        self.location = location
        if long_description is not None:
          self.long_description = long_description
        if mime_type is not None:
          self.mime_type = mime_type
        self.name = name
        if priority is not None:
          self.priority = priority
        if privacy is not None:
          self.privacy = privacy
        if published is not None:
          self.published = published
        if short_description is not None:
          self.short_description = short_description
        if size is not None:
          self.size = size
        if tags is not None:
          self.tags = tags
        if thumbnail is not None:
          self.thumbnail = thumbnail
        if updated_date is not None:
          self.updated_date = updated_date
        if uploader is not None:
          self.uploader = uploader
        if views is not None:
          self.views = views
        self.width = width

    @property
    def active(self):
        """
        Gets the active of this VideoResource.
        Whether the video is available, based on various factors

        :return: The active of this VideoResource.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this VideoResource.
        Whether the video is available, based on various factors

        :param active: The active of this VideoResource.
        :type: bool
        """

        self._active = active

    @property
    def author(self):
        """
        Gets the author of this VideoResource.
        The original artist of the media

        :return: The author of this VideoResource.
        :rtype: SimpleReferenceResourcelong
        """
        return self._author

    @author.setter
    def author(self, author):
        """
        Sets the author of this VideoResource.
        The original artist of the media

        :param author: The author of this VideoResource.
        :type: SimpleReferenceResourcelong
        """

        self._author = author

    @property
    def authored(self):
        """
        Gets the authored of this VideoResource.
        The date the media was created as a unix timestamp in seconds

        :return: The authored of this VideoResource.
        :rtype: int
        """
        return self._authored

    @authored.setter
    def authored(self, authored):
        """
        Sets the authored of this VideoResource.
        The date the media was created as a unix timestamp in seconds

        :param authored: The authored of this VideoResource.
        :type: int
        """

        self._authored = authored

    @property
    def banned(self):
        """
        Gets the banned of this VideoResource.
        Whether the video has been banned or not

        :return: The banned of this VideoResource.
        :rtype: bool
        """
        return self._banned

    @banned.setter
    def banned(self, banned):
        """
        Sets the banned of this VideoResource.
        Whether the video has been banned or not

        :param banned: The banned of this VideoResource.
        :type: bool
        """

        self._banned = banned

    @property
    def category(self):
        """
        Gets the category of this VideoResource.
        The category of the video

        :return: The category of this VideoResource.
        :rtype: SimpleReferenceResourcestring
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this VideoResource.
        The category of the video

        :param category: The category of this VideoResource.
        :type: SimpleReferenceResourcestring
        """
        if category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")

        self._category = category

    @property
    def comments(self):
        """
        Gets the comments of this VideoResource.
        The comments of the video

        :return: The comments of this VideoResource.
        :rtype: list[CommentResource]
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this VideoResource.
        The comments of the video

        :param comments: The comments of this VideoResource.
        :type: list[CommentResource]
        """

        self._comments = comments

    @property
    def contributors(self):
        """
        Gets the contributors of this VideoResource.
        Artists that contributed to the creation. See separate endpoint to add to list

        :return: The contributors of this VideoResource.
        :rtype: list[ContributionResource]
        """
        return self._contributors

    @contributors.setter
    def contributors(self, contributors):
        """
        Sets the contributors of this VideoResource.
        Artists that contributed to the creation. See separate endpoint to add to list

        :param contributors: The contributors of this VideoResource.
        :type: list[ContributionResource]
        """

        self._contributors = contributors

    @property
    def created_date(self):
        """
        Gets the created_date of this VideoResource.
        The date/time this resource was created in seconds since unix epoch

        :return: The created_date of this VideoResource.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this VideoResource.
        The date/time this resource was created in seconds since unix epoch

        :param created_date: The created_date of this VideoResource.
        :type: int
        """

        self._created_date = created_date

    @property
    def embed(self):
        """
        Gets the embed of this VideoResource.
        The country of an embedable version

        :return: The embed of this VideoResource.
        :rtype: str
        """
        return self._embed

    @embed.setter
    def embed(self, embed):
        """
        Sets the embed of this VideoResource.
        The country of an embedable version

        :param embed: The embed of this VideoResource.
        :type: str
        """

        self._embed = embed

    @property
    def extension(self):
        """
        Gets the extension of this VideoResource.
        The file extension of the media file. 1-5 characters

        :return: The extension of this VideoResource.
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """
        Sets the extension of this VideoResource.
        The file extension of the media file. 1-5 characters

        :param extension: The extension of this VideoResource.
        :type: str
        """
        if extension is None:
            raise ValueError("Invalid value for `extension`, must not be `None`")

        self._extension = extension

    @property
    def height(self):
        """
        Gets the height of this VideoResource.
        The height of the video in px

        :return: The height of this VideoResource.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this VideoResource.
        The height of the video in px

        :param height: The height of this VideoResource.
        :type: int
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")

        self._height = height

    @property
    def id(self):
        """
        Gets the id of this VideoResource.
        The unique ID for that resource

        :return: The id of this VideoResource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VideoResource.
        The unique ID for that resource

        :param id: The id of this VideoResource.
        :type: int
        """

        self._id = id

    @property
    def length(self):
        """
        Gets the length of this VideoResource.
        The length of the video in seconds

        :return: The length of this VideoResource.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """
        Sets the length of this VideoResource.
        The length of the video in seconds

        :param length: The length of this VideoResource.
        :type: int
        """
        if length is None:
            raise ValueError("Invalid value for `length`, must not be `None`")

        self._length = length

    @property
    def location(self):
        """
        Gets the location of this VideoResource.
        The country of the media. Typically a url. Cannot be blank

        :return: The location of this VideoResource.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this VideoResource.
        The country of the media. Typically a url. Cannot be blank

        :param location: The location of this VideoResource.
        :type: str
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")

        self._location = location

    @property
    def long_description(self):
        """
        Gets the long_description of this VideoResource.
        The user friendly name of that resource. Defaults to blank string

        :return: The long_description of this VideoResource.
        :rtype: str
        """
        return self._long_description

    @long_description.setter
    def long_description(self, long_description):
        """
        Sets the long_description of this VideoResource.
        The user friendly name of that resource. Defaults to blank string

        :param long_description: The long_description of this VideoResource.
        :type: str
        """

        self._long_description = long_description

    @property
    def mime_type(self):
        """
        Gets the mime_type of this VideoResource.
        The mime-type of the media

        :return: The mime_type of this VideoResource.
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """
        Sets the mime_type of this VideoResource.
        The mime-type of the media

        :param mime_type: The mime_type of this VideoResource.
        :type: str
        """

        self._mime_type = mime_type

    @property
    def name(self):
        """
        Gets the name of this VideoResource.
        The user friendly name of that resource

        :return: The name of this VideoResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VideoResource.
        The user friendly name of that resource

        :param name: The name of this VideoResource.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def priority(self):
        """
        Gets the priority of this VideoResource.
        The sort order of the video. default: 100

        :return: The priority of this VideoResource.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this VideoResource.
        The sort order of the video. default: 100

        :param priority: The priority of this VideoResource.
        :type: int
        """

        self._priority = priority

    @property
    def privacy(self):
        """
        Gets the privacy of this VideoResource.
        The privacy setting. default: private

        :return: The privacy of this VideoResource.
        :rtype: str
        """
        return self._privacy

    @privacy.setter
    def privacy(self, privacy):
        """
        Sets the privacy of this VideoResource.
        The privacy setting. default: private

        :param privacy: The privacy of this VideoResource.
        :type: str
        """
        allowed_values = ["private", "friends", "public"]
        if privacy not in allowed_values:
            raise ValueError(
                "Invalid value for `privacy` ({0}), must be one of {1}"
                .format(privacy, allowed_values)
            )

        self._privacy = privacy

    @property
    def published(self):
        """
        Gets the published of this VideoResource.
        Whether the video has been made public. Default true

        :return: The published of this VideoResource.
        :rtype: bool
        """
        return self._published

    @published.setter
    def published(self, published):
        """
        Sets the published of this VideoResource.
        Whether the video has been made public. Default true

        :param published: The published of this VideoResource.
        :type: bool
        """

        self._published = published

    @property
    def short_description(self):
        """
        Gets the short_description of this VideoResource.
        The user friendly name of that resource. Defaults to blank string

        :return: The short_description of this VideoResource.
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """
        Sets the short_description of this VideoResource.
        The user friendly name of that resource. Defaults to blank string

        :param short_description: The short_description of this VideoResource.
        :type: str
        """

        self._short_description = short_description

    @property
    def size(self):
        """
        Gets the size of this VideoResource.
        The size of the media. Minimum 0 if supplied

        :return: The size of this VideoResource.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this VideoResource.
        The size of the media. Minimum 0 if supplied

        :param size: The size of this VideoResource.
        :type: int
        """

        self._size = size

    @property
    def tags(self):
        """
        Gets the tags of this VideoResource.
        The tags for the video

        :return: The tags of this VideoResource.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this VideoResource.
        The tags for the video

        :param tags: The tags of this VideoResource.
        :type: list[str]
        """

        self._tags = tags

    @property
    def thumbnail(self):
        """
        Gets the thumbnail of this VideoResource.
        The country of a thumbnail version. Typically a url

        :return: The thumbnail of this VideoResource.
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """
        Sets the thumbnail of this VideoResource.
        The country of a thumbnail version. Typically a url

        :param thumbnail: The thumbnail of this VideoResource.
        :type: str
        """

        self._thumbnail = thumbnail

    @property
    def updated_date(self):
        """
        Gets the updated_date of this VideoResource.
        The date/time this resource was last updated in seconds since unix epoch

        :return: The updated_date of this VideoResource.
        :rtype: int
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """
        Sets the updated_date of this VideoResource.
        The date/time this resource was last updated in seconds since unix epoch

        :param updated_date: The updated_date of this VideoResource.
        :type: int
        """

        self._updated_date = updated_date

    @property
    def uploader(self):
        """
        Gets the uploader of this VideoResource.
        The user the media was uploaded by. May be null for system uploaded media. May only be set to a user other than the current caller if VIDEOS_ADMIN permission. Null will mean the caller is the uploader unless the caller has VIDEOS_ADMIN permission, in which case it will be set to null

        :return: The uploader of this VideoResource.
        :rtype: SimpleUserResource
        """
        return self._uploader

    @uploader.setter
    def uploader(self, uploader):
        """
        Sets the uploader of this VideoResource.
        The user the media was uploaded by. May be null for system uploaded media. May only be set to a user other than the current caller if VIDEOS_ADMIN permission. Null will mean the caller is the uploader unless the caller has VIDEOS_ADMIN permission, in which case it will be set to null

        :param uploader: The uploader of this VideoResource.
        :type: SimpleUserResource
        """

        self._uploader = uploader

    @property
    def views(self):
        """
        Gets the views of this VideoResource.
        The view count of the video

        :return: The views of this VideoResource.
        :rtype: int
        """
        return self._views

    @views.setter
    def views(self, views):
        """
        Sets the views of this VideoResource.
        The view count of the video

        :param views: The views of this VideoResource.
        :type: int
        """

        self._views = views

    @property
    def width(self):
        """
        Gets the width of this VideoResource.
        The width of the video in px

        :return: The width of this VideoResource.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this VideoResource.
        The width of the video in px

        :param width: The width of this VideoResource.
        :type: int
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")

        self._width = width

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, VideoResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other