from p_files import average_by, tail, word_count


def test_word_count(tmp_path):
    path = tmp_path / "t.txt"
    path.write_text("one two\n  three\n\nfour\n")
    assert word_count(path) == 4


def test_tail(tmp_path):
    path = tmp_path / "t.txt"
    path.write_text("a\nb\nc\nd\n")
    assert tail(path, 2) == ["c", "d"]
    assert tail(path, 10) == ["a", "b", "c", "d"]
    assert tail(path, 0) == []


def test_average_by(tmp_path):
    path = tmp_path / "grades.csv"
    path.write_text("section,score\nA,90\nB,70\nA,80\n")
    assert average_by(path, "section", "score") == {"A": 85.0, "B": 70.0}
