# Personal Site

## Add post

```
hugo new posts/my-post.md
```

## Deploy

Based on directions here: https://gohugo.io/hosting-and-deployment/hosting-on-github/

```
./deploy.sh "message"
```



## Getting Started

### Install Hugo

```
brew install hugo
```

### Build Locally 

```
hugo --watch
```

### Serve

```
python -m http.server 8080 --bind 127.0.0.1 --directory public/
```
