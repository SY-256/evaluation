# TPR: 再現率と同じ
# TPR = recall = TP / (TP + FN)
# TPRや再現率は"感度"と呼ばれる

from recall_score import recall

def tpr_value(y_true, y_pred):
    """TPRを計算する関数
    Args:
        y_true: 正解のリスト
        y_pred: 予測値のリスト
        return: TPR
    """
    tpr = recall(y_true, y_pred)
    return tpr