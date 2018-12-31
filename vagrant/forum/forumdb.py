# "Database code" for the DB Forum.

import datetime
import psycopg2
import bleach

bleach.clean('an <script>evil()</script> example')
u'an &lt;script&gt;evil()&lt;/script&gt; example'
bleach.linkify('an http://example.com url')
u'an <a href="http://example.com" rel="nofollow">http://example.com</a> url'

#POSTS = [("This is the first post.", datetime.datetime.now())]

DBNAME = "forum"

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database = DBNAME)

  cursor = db.cursor()
  cursor.execute ("select content, time from posts order by time desc")
  #return reversed(POSTS)
  post = cursor.fetchall()
  db.close()
  return post

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  #POSTS.append((content, datetime.datetime.now()))

  db = psycopg2.connect(database = DBNAME)
  cursor = db.cursor()
  #cursor.execute ("insert into posts values {}".format(content,))

  cursor.execute ("insert into posts values (%s)",  (content,))
  #cursor.execute ("insert into posts values content")

  db.commit()

  db.close()



