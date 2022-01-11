# Personal Site

## Add post

```
hugo new posts/my-post.md
```

## Deploy

Deployment are automated based on push to `master` branch. That kicks off a github action that publishes the public artifacts to `gh-pages` branch, which is what GitHub hosts.


## Working locally

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
