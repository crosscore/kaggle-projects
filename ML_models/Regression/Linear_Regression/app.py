from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import matplotlib.pyplot as plt
import io
import base64
from starlette.responses import Response

app = FastAPI()

model = joblib.load('model.joblib')

class InputData(BaseModel):
    x: float

class PredictionResult(BaseModel):
    prediction: float
    plot: str  # Base64エンコードされた画像データ

@app.post("/predict", response_model=PredictionResult)
async def predict(data: InputData):
    """
    入力された数値に基づいて予測を行い、グラフと共に結果を返すAPIエンドポイント
    """
    try:
        # 予測の実行
        x = data.x
        prediction = model.predict([[x]])[0]

        # グラフの作成
        # Xの範囲を少し広げて、予測値が範囲内に収まるようにする
        X_range = [[-1], [7]]
        y_range = model.predict(X_range)

        plt.figure()
        plt.scatter([x_val[0] for x_val in X], y, color='blue', label='Training Data')  # トレーニングデータを青い点でプロット
        plt.plot(X_range, y_range, color='red', label='Regression Line')  # 回帰直線を赤い線でプロット
        plt.scatter([x], [prediction], color='green', label='Prediction')  # 予測値を緑の点でプロット
        plt.xlabel('X')
        plt.ylabel('y')
        plt.title('Linear Regression')
        plt.legend() # 凡例を表示
        plt.grid(True)

        # グラフをBase64エンコードして文字列に変換
        img = io.BytesIO()
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()

        return {"prediction": prediction, "plot": plot_url}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/plot/{plot_data}")
async def get_plot(plot_data: str):
    """
    Base64エンコードされた画像データをデコードして画像として返す
    """
    try:
        # Base64デコード
        img_data = base64.b64decode(plot_data)
        return Response(content=img_data, media_type="image/png")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
