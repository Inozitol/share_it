# share_it
A Python script that will create symlink to your webserver for sharing some files very quickly.

#### Example:
* ```shareit ~/Pictures/nice_picture.jpg```
* ```shareit ~/Documents/important_doc.doc --port 443```
* ```shareit ~/Documents/alsoimportant.doc -P```

#### Parameters:
* **--port** | **-p** Changes what port should be used
* **-P** Uses an API to test if the port is open

#### TODO:
- [x] Add ability to test ports
- [ ] Parameter for target folder
- [ ] Config for target folder
- [ ] Better handling of HTTPS
