from hello import main


def test_hello_application(capsys):
    main()

    captured = capsys.readouterr()

    assert "Hello, MLOps!" in captured.out
    assert "Python application executed successfully." in captured.out