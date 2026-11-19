---
layout: default
title: Amorolfine
parent: 僅模型預測 (L5)
nav_order: 57
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-17
description: "Amorolfine：預測新適應症為藥物誘發性骨質疏鬆 (drug-induced osteoporosis)（證據等級 L5）。原適應症：指甲真菌感染"
monitor_inn: "Amorolfine"
predicted_indications: ["drug-induced osteoporosis", "disease of retroperitoneum", "disease of uterine broad ligament", "lumbar spinal stenosis", "abdominal ectopic pregnancy", "abdominal cystic lymphangioma", "celiac trunk compression syndrome", "sacrum chordoma", "lymph node palisaded myofibroblastoma", "urethral disease"]
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

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Amorolfine：從局部抗真菌治療到藥物誘發性骨質疏鬆（模型預測）
{: .text-alpha }

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
| TxGNN 預測分數 | 1.0000 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 21 張／共 21 張） |
| 許可證數 | 21 張（有效 21 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏經確認的作用機轉資料。就已知藥理而言，amorolfine 是外用嗎啉類抗真菌藥，
作用於真菌麥角固醇（ergosterol）合成途徑，抑制 Δ14 還原酶與 Δ7,8 異構酶，
使真菌細胞膜結構受損。

這個機轉與骨代謝之間**沒有已知的關聯**。藥物誘發性骨質疏鬆與長期使用糖皮質激素等藥物導致骨量流失有關，
而 amorolfine 為局部外用，全身暴露量極低，進一步降低其作用於骨骼的可能性。
因此，這項預測的分數來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，而非生物學證據。

其餘排名前十的預測（腹膜後疾病、子宮闊韌帶疾病、腰椎管狹窄、腹腔異位妊娠、腹腔動脈壓迫症候群、腹部囊性淋巴管瘤、淋巴結柵欄狀肌纖維母細胞瘤、骶骨脊索瘤、尿道疾病）同樣沒有機轉依據，也沒有任何試驗或文獻支持。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 21 張含本藥成分的許可證（全部有效；皆為單一成分）。以下列出 5 張主要許可證，其餘以各品牌同成分製劑登記。

<!-- review:begin hk-lic-20261117-amorolfine-1 -->

> **查核更正（2026-11-17）**：原文為「本藥在香港共有 20 張有效單方許可證（無已註銷者）。」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊：共有 21 張含本藥成分的許可證（全部有效；皆為單一成分）（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-amorolfine-1 -->

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
- 預測分數雖高（1.0000），但沒有任何臨床試驗或文獻佐證，證據等級僅為 L5。
- 作用機轉與骨代謝無已知關聯，且外用製劑全身暴露極低，預測合理性很低。

**若要推進需要：**
- 補齊作用機轉資料，並評估是否存在任何與骨代謝相關的途徑。
- 進行系統性文獻與前臨床檢索，確認是否有支持性訊號。
- 補充香港仿單的警語與禁忌症資料，以便進行安全性篩選。
- 評估外用劑型是否能達到足夠的全身暴露量（路徑相容性目前尚待評估）。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「本藥在香港共有 20 張有效單方許可證（無已註銷者）。」→「香港共有 21 張含本藥成分的許可證（全部有效；皆為單一成分」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

