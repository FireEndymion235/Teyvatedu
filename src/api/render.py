from models import Notification
from models import Book
from webcore import utils
async def render_notifications():
    boxes = await Notification.Notification.all()
    all_text = ""
    boxes.sort(key=lambda x: x.datetime.ctime(), reverse=True)  # ranking by latest
    for box in boxes:
         # precheck can be done here
        all_text += f"""
    <div class="box">
    <h3>{box.title}</h3>
    <p>{box.content}</p>
    <img src="static/images/{box.img}" style="width: 100%;" alt="" />
    <p style="direction: rtl;">{box.publish}<br>{utils.convert_datetime(str(box.datetime))}</p>
    </div>
    """
    return all_text
async def render_books():
    bookes = await Book.Book.all()
    all_text = ""
    for book in bookes:
        all_text += f"""<article>
		<h2>{book.title}</h2>
		<img src="static/images/{book.img}" alt="" style="width: 100%;" />
		<h4>{book.author}</h4>
		<p>{book.desc}</p>
		<p>{book.content}</p>
        <p>{book.group}</p>
        <ul class="actions">
			<li><a href="/singlebook?id={book.id}" class="button" style="font-family: 'GSFont';">查看详情</a></li>
		</ul>
		</article>"""
    return all_text