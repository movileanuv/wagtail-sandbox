* Follow the commit history for a step by step introduction
* More on StreamFields: https://docs.wagtail.org/en/stable/topics/streamfield.html#limiting-block-counts
* Accessing data on StreamFields and reset to empty:
  ```python
  from pages.models import HomePage
  
  >>> p = HomePage.objects.first()
  >>> p.body.raw_data
  [{'type': 'paragraph', 'value': '<h2 data-block-key="luugi">Hello, world!</h2><p data-block-key="mjuh">Suspendisse non nisl sit amet velit hendrerit rutrum. Phasellus gravida semper nisi. Phasellus nec sem in justo pellentesque facilisis. Nam eget dui.</p>', 'id': '618fff67-e34d-46c6-8ba0-3144dc92fadf'}, {'type': 'image', 'value': 1, 'id': 'a411fd03-281a-48ed-9dae-22ff34a42ac4'}, {'type': 'document', 'value': 1, 'id': 'b6a33d42-a27b-42f9-a0ca-ddf7b3d46477'}, {'type': 'person', 'value': {'first_name': 'Victor', 'surname': 'Movileanu', 'photo': 2, 'biography': '<p data-block-key="05u0u">Cras risus ipsum, faucibus ut, ullamcorper id, varius ac, leo. Donec vitae sapien ut libero venenatis faucibus. Nunc interdum lacus sit amet orci. Nunc sed turpis.</p>'}, 'id': '6db8585d-21f5-458c-bbcc-11f873fa1d79'}, {'type': 'gallery', 'value': [{'type': 'item', 'value': 2, 'id': '23e78e59-677a-4192-8365-fde5c5b7c21b'}, {'type': 'item', 'value': 1, 'id': '2fcf3911-8c6b-4872-94f4-83f7943f773b'}, {'type': 'item', 'value': 2, 'id': '428e5f3f-c55a-4b56-b9c3-72273a265309'}, {'type': 'item', 'value': 1, 'id': '6cf3d63e-3b78-431e-bf53-495c8e7262a5'}], 'id': '0a8731c8-c5c7-47c4-bb6b-111fb05d3fed'}]
  >>> p.body.raw_data = []
  >>> p.save()
  ```
* Wagtail Internationalization: https://docs.wagtail.org/en/stable/advanced_topics/i18n.html
* Wagtail localize: https://www.wagtail-localize.org/how-to/field-configuration/
