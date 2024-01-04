def AI():
            import wolframalpha
            app_id = "RQ43J4-LJ8G54LL3K"
            client = wolframalpha.Client(app_id)
            res = client.query("hey jarvis what is 2 multiplied by 2")
            answ = next(res.results).text
            print(answ)
AI()