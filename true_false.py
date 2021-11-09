# TP（真陽性）, TN（真陰性）, FP（偽陽性）, FN（偽陰性）
def true_positive(y_true, y_pred) -> int:
    """真陽性を計算する関数
    Args:
        y_true: 正解のリスト
        y_pred: 予測値のリスト
        return: 真陽性の数
    """
    # 初期化
    tp = 0
    for yt, yp in zip(y_true, y_pred):
        if yt == 1 and yp == 1:
            tp += 1
    return tp

def true_negative(y_true, y_pred) -> int:
    """真陰性を計算する関数
    Args:
        y_true: 正解のリスト
        y_pred: 予測値のリスト
        return: 真陰性の数
    """
    # 初期化
    tn = 0
    for yt, yp in zip(y_true, y_pred):
        if yt == 0 and yp == 0:
            tn += 1
    return tn

def false_positive(y_true, y_pred) -> int:
    """偽陽性を計算する関数
    Args:
        y_true: 正解のリスト
        y_pred: 予測値のリスト
        return: 偽陽性の数
    """
    # 初期化
    fp = 0
    for yt, yp in zip(y_true, y_pred):
        if yt == 0 and yp == 1:
            fp += 1
    return fp

def false_negative(y_true, y_pred) -> int:
    """偽陰性を計算する関数
    Args:
        y_true: 正解のリスト
        y_pred: 予測値のリスト
        return: 偽陰性の数
    """
    # 初期化
    fn = 0
    for yt, yp in zip(y_true, y_pred):
        if yt == 1 and yp == 0:
            fn += 1
    return fn