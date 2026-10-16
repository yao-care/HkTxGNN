---
layout: default
title: Amorolfine
parent: 僅模型預測 (L5)
nav_order: 57
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Amorolfine：預測新適應症為藥物誘發性骨質疏鬆 (drug-induced osteoporosis)（證據等級 L5）。原適應症：指甲真菌感染"
monitor_inn: "Amorolfine"
predicted_indications: ["drug-induced osteoporosis", "disease of retroperitoneum", "disease of uterine broad ligament", "lumbar spinal stenosis", "abdominal ectopic pregnancy", "celiac trunk compression syndrome", "abdominal cystic lymphangioma", "lymph node palisaded myofibroblastoma", "sacrum chordoma", "urethral disease"]
---

# Amorolfine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Amorolfine：從局部抗真菌治療到藥物誘發性骨質疏鬆（模型預測）

## 一句話總結

Amorolfine 是外用嗎啉類（morpholine）抗真菌藥，臨床上用於治療指甲真菌感染（甲癬）。
TxGNN 模型預測它可能對**藥物誘發性骨質疏鬆 (drug-induced osteoporosis)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅屬模型推論，建議暫緩（Hold）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 指甲真菌感染（甲癬，依藥物資料推斷；香港許可證資料未載明適應症文字） |
| 預測新適應症 | 藥物誘發性骨質疏鬆 (drug-induced osteoporosis) |
| TxGNN 預測分數 | 99.998% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏經確認的作用機轉資料。就已知藥理而言，amorolfine 是外用嗎啉類抗真菌藥，
作用於真菌麥角固醇（ergosterol）合成途徑，抑制 Δ14 還原酶與 Δ7,8 異構酶，
使真菌細胞膜結構受損。

這個機轉與骨代謝之間**沒有已知的關聯**。藥物誘發性骨質疏鬆與長期使用糖皮質激素等藥物導致骨量流失有關，
而 amorolfine 為局部外用，全身暴露量極低，進一步降低其作用於骨骼的可能性。
因此，這項預測較可能是知識圖譜結構所產生的結果，而非真實的藥理訊號。

其餘排名前十的預測（腹膜後疾病、子宮闊韌帶疾病、腰椎管狹窄、腹腔異位妊娠、腹腔動脈壓迫症候群、腹部囊性淋巴管瘤、淋巴結柵欄狀肌纖維母細胞瘤、骶骨脊索瘤、尿道疾病）同樣沒有機轉依據，也沒有任何試驗或文獻支持。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

本藥在香港共有 20 張有效單方許可證（無已註銷者）。以下列出 5 張主要許可證，其餘以各品牌同成分製劑登記。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-36522 | LOCERYL NAIL LACQUER 5%（Galderma） | 指甲油（外用） | 許可證資料未載明 |
| HK-51795 | LOCERYL CREAM 0.25%W/W（Galderma） | 乳膏（外用） | 許可證資料未載明 |
| HK-61679 | AMOROLFINE NAIL LACQUER 5% W/V（Hind Wing） | 指甲油（外用） | 許可證資料未載明 |
| HK-66253 | LOMORYL CREAM 2.5MG/G（Julius Chen） | 乳膏（外用） | 許可證資料未載明 |
| HK-63856 | PHARMA AMOROLFINE NAIL LACQUER 5% W/V（LSB） | 指甲油（外用） | 許可證資料未載明 |

---

## 安全性考量

- **藥物交互作用**：藥理資料庫顯示 amorolfine 與電壓門控鈉離子通道 Nav1.7 (SCN9A) 有交互作用紀錄，但未標示嚴重程度，臨床意義不明。

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高（99.998%），但沒有任何臨床試驗或文獻佐證，證據等級僅為 L5。
- 作用機轉與骨代謝無已知關聯，且外用製劑全身暴露極低，預測合理性很低。

**若要推進需要：**
- 補齊作用機轉資料，並評估是否存在任何與骨代謝相關的途徑。
- 進行系統性文獻與前臨床檢索，確認是否有支持性訊號。
- 補充香港仿單的警語與禁忌症資料，以便進行安全性篩選。
- 評估外用劑型是否能達到足夠的全身暴露量（路徑相容性目前尚待評估）。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

