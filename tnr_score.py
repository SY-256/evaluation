# 1-FPRは特異度またはTNR(True Negative Rate)

from fpr_score import fpr_value

def tnr_value(y_true, y_pred):
    """TNRを計算する関数
    Args:
        y_true: 正解のリスト
        y_pred: 予測値のリスト
        return: TNR
    """
    # 偽陽性率
    fpr = fpr_value(y_true, y_pred)
    
    # 特異度(真陰性率)
    tnr = 1 - fpr
    
    return tnr