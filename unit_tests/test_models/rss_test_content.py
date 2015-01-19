
rss_test_content_head = """<?xml version="1.0" encoding="utf-8" ?>
		<rss version="2.0" xmlns:dc="http://purl.org/dc/elements/1.1/">
		<channel>
		<title>linux_distros.com</title>
		<description>linux_distros.com RSS()</description>
		<link>http://linux_distros.com</link><image>
		<url>http://linux_distros.com/favicon.ico</url>
		<link>http://linux_distros.com</link></image>
"""

rss_test_content_items = [
"""<item>
<title>House of Lies - 4x02 [HDTV-720p - Eng - BATV]</title>
<pubDate>Mon, 12 Jan 2015 18:34:33 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=140858</guid>
<description>-</description>
<category>House of Lies</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=140858&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>House of Lies - 4x01 [HDTV-720p - Eng - BATV]</title>
<pubDate>Fri, 09 Jan 2015 19:00:27 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=140734</guid>
<description>-</description>
<category>House of Lies</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=140734&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>House of Lies - 4x01 [HDTV-720p - Eng - IMMERSE]</title>
<pubDate>Fri, 09 Jan 2015 13:39:34 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=140713</guid>
<description>-</description>
<category>House of Lies</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=140713&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>Homeland - 4x12 - INTERNAL [HDTV-720p - Eng - BATV]</title>
<pubDate>Mon, 22 Dec 2014 14:20:43 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=140111</guid>
<description>-</description>
<category>Homeland</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=140111&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>Homeland - 4x12 [HDTV-720p - Eng - IMMERSE]</title>
<pubDate>Mon, 22 Dec 2014 13:51:52 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=140102</guid>
<description>-</description>
<category>Homeland</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=140102&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>Homeland - 4.evad/12 [HDTV-720p - Eng]</title>
<pubDate>Mon, 22 Dec 2014 11:05:14 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=140096</guid>
<description>-</description>
<category>Homeland</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=140096&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>The 100 - 2x08 [HDTV-720p - Eng - DIMENSION]</title>
<pubDate>Thu, 18 Dec 2014 04:03:43 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=139955</guid>
<description>-</description>
<category>The 100</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=139955&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>Homeland - 4x11 [HDTV-720p - Eng - KILLERS]</title>
<pubDate>Mon, 15 Dec 2014 03:53:36 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=139830</guid>
<description>-</description>
<category>Homeland</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=139830&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>Z Nation - 1.evad/13 [HDTV-720p - Eng]</title>
<pubDate>Sat, 13 Dec 2014 12:24:05 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=139780</guid>
<description>-</description>
<category>Z Nation</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=139780&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>The 100 - 2x07 [HDTV-720p - Eng - KILLERS]</title>
<pubDate>Thu, 11 Dec 2014 04:12:32 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=139634</guid>
<description>-</description>
<category>The 100</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=139634&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>Marvel's Agents of S.H.I.E.L.D. - 2x10 [HDTV-720p - Eng - KILLERS]</title>
<pubDate>Wed, 10 Dec 2014 04:07:43 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=139556</guid>
<description>-</description>
<category>Marvel's Agents of S.H.I.E.L.D.</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=139556&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>Homeland - 4x10 [HDTV-720p - Eng - KILLERS]</title>
<pubDate>Mon, 08 Dec 2014 09:04:13 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=139437</guid>
<description>-</description>
<category>Homeland</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=139437&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>The 100 - 2x06 [HDTV-720p - Eng - KILLERS]</title>
<pubDate>Thu, 04 Dec 2014 06:28:07 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=139216</guid>
<description>-</description>
<category>The 100</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=139216&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>Marvel's Agents of S.H.I.E.L.D. - 2x09 [HDTV-720p - Eng - KILLERS]</title>
<pubDate>Wed, 03 Dec 2014 12:00:12 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=139171</guid>
<description>-</description>
<category>Marvel's Agents of S.H.I.E.L.D.</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=139171&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>The Walking Dead - 5x08 [REPACK HDTV-720p - Eng - KILLERS]</title>
<pubDate>Mon, 01 Dec 2014 04:29:15 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=139077</guid>
<description>-</description>
<category>The Walking Dead</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=139077&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>The Walking Dead - 5x07 [HDTV-720p - Eng - KILLERS]</title>
<pubDate>Mon, 24 Nov 2014 11:42:15 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=138678</guid>
<description>-</description>
<category>The Walking Dead</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=138678&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>Homeland - 4x09 [HDTV-720p - Eng - KILLERS]</title>
<pubDate>Mon, 24 Nov 2014 11:23:45 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=138671</guid>
<description>-</description>
<category>Homeland</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=138671&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>The 100 - 2x05 [HDTV-720p - Eng - KILLERS]</title>
<pubDate>Thu, 20 Nov 2014 04:13:33 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=138425</guid>
<description>-</description>
<category>The 100</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=138425&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>Marvel's Agents of S.H.I.E.L.D. - 2x08 [REPACK HDTV-720p - Eng - KILLERS]</title>
<pubDate>Wed, 19 Nov 2014 16:36:17 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=138387</guid>
<description>-</description>
<category>Marvel's Agents of S.H.I.E.L.D.</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=138387&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>Marvel's Agents of S.H.I.E.L.D. - 2x08 [HDTV-720p - Eng - KILLERS]</title>
<pubDate>Wed, 19 Nov 2014 04:42:23 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=138358</guid>
<description>-</description>
<category>Marvel's Agents of S.H.I.E.L.D.</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=138358&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>The Walking Dead - 5x06 [HDTV-720p - Eng - DIMENSION]</title>
<pubDate>Mon, 17 Nov 2014 04:15:07 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=138226</guid>
<description>-</description>
<category>The Walking Dead</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=138226&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>Homeland - 4x08 [HDTV-720p - Eng - KILLERS]</title>
<pubDate>Mon, 17 Nov 2014 04:03:41 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=138224</guid>
<description>-</description>
<category>Homeland</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=138224&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>The 100 - 2x04 [HDTV-720p - Eng - KILLERS]</title>
<pubDate>Thu, 13 Nov 2014 04:10:41 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=137943</guid>
<description>-</description>
<category>The 100</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=137943&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>Marvel's Agents of S.H.I.E.L.D. - 2x07 [HDTV-720p - Eng - KILLERS]</title>
<pubDate>Wed, 12 Nov 2014 04:06:19 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=137842</guid>
<description>-</description>
<category>Marvel's Agents of S.H.I.E.L.D.</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=137842&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>The Walking Dead - 5x05 [HDTV-720p - Eng - KILLERS]</title>
<pubDate>Mon, 10 Nov 2014 04:19:19 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=137684</guid>
<description>-</description>
<category>The Walking Dead</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=137684&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>Homeland - 4x07 [HDTV-720p - Eng - KILLERS]</title>
<pubDate>Mon, 10 Nov 2014 03:56:39 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=137675</guid>
<description>-</description>
<category>Homeland</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=137675&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>The 100 - 2x03 [HDTV-720p - Eng - DIMENSION]</title>
<pubDate>Thu, 06 Nov 2014 04:15:02 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=137429</guid>
<description>-</description>
<category>The 100</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=137429&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>The Walking Dead - 5x04 [HDTV-720p - Eng - KILLERS]</title>
<pubDate>Mon, 03 Nov 2014 04:08:13 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=137258</guid>
<description>-</description>
<category>The Walking Dead</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=137258&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>Homeland - 4x06 [HDTV-720p - Eng - KILLERS]</title>
<pubDate>Mon, 03 Nov 2014 03:53:14 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=137251</guid>
<description>-</description>
<category>Homeland</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=137251&amp;uid=456789&amp;passkey=42</link>
</item>""",
"""<item>
<title>The 100 - 2x02 [HDTV-720p - Eng - DIMENSION]</title>
<pubDate>Thu, 30 Oct 2014 07:29:16 +0100</pubDate>
<guid>http://linux_distros.com/torrent/browse.php?id=137025</guid>
<description>-</description>
<category>The 100</category>
<link>http://linux_distros.com/torrent/download.php?type=rss&amp;id=137025&amp;uid=456789&amp;passkey=42</link>
</item>"""]

rss_test_content_foot = """
</channel>
</rss>
"""