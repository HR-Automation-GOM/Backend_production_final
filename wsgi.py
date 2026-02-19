# from app import create_app
# app = create_app()
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
```

---

## After Committing

Railway will auto-redeploy. You should see:
```
✅ Detected Python
✅ Using pip  
✅ Starting with gunicorn wsgi:app
✅ Deploy successful
