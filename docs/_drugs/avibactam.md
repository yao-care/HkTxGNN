---
layout: default
title: Avibactam
parent: 僅模型預測 (L5)
nav_order: 88
evidence_level: L5
indication_count: 4
monitor_inn: "Avibactam"
predicted_indications: ["ureter tuberculosis", "urinary schistosomiasis", "hyperamylasemia", "polyclonal hyperviscosity syndrome"]
last_modified_at: 2026-10-28
description: "Avibactam：預測新適應症為泌尿道結核 (ureter tuberculosis)（證據等級 L5）。原適應症：腎盂腎炎"
---

# Avibactam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

## Avibactam：從腎盂腎炎到泌尿道結核（ureter tuberculosis）
{: .text-alpha }

## 一句話總結

Avibactam 是一種 β-內醯胺酶抑制劑，在知識圖譜中記錄的原適應症為腎盂腎炎。
TxGNN 模型預測它可能對**泌尿道結核 (ureter tuberculosis)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持，僅屬模型預測層級。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 腎盂腎炎（知識圖譜中記錄的關聯；香港許可證資料未載明適應症文字） |
| 預測新適應症 | 泌尿道結核 (ureter tuberculosis) |
| TxGNN 預測分數 | 0.9911 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Avibactam 是非 β-內醯胺類（diazabicyclooctane）的 β-內醯胺酶抑制劑，通常與搭配的 β-內醯胺類抗生素（如 ceftazidime）合用，用來恢復其對 Ambler A、C 類及部分 D 類酵素產生菌的活性。

結核分枝桿菌具有染色體編碼的 A 類 β-內醯胺酶（BlaC），Avibactam 在體外對 BlaC 有抑制活性，因此理論上存在機轉關聯。不過，這需要搭配具抗分枝桿菌活性的 β-內醯胺類藥物才有意義，且尚未在泌尿生殖道結核得到臨床驗證。

TxGNN 的高分（0.9911）僅是模型輸出，不等同於實際療效。另外，本報告彙整的資料中也缺乏 Avibactam 的作用機轉記錄。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66061 | ZAVICEFTA POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 2G/0.5G | 未載明 | 未載明 |
| HK-68891 | EMBLAVEO POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 1.5G/0.5G | 未載明 | 未載明 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何研究直接探討 Avibactam 用於泌尿道結核，證據等級僅為 L5，且高預測分數只是模型輸出。
- 雖然 BlaC 抑制提供理論上的機轉線索，但需要有抗分枝桿菌活性的搭配藥物，臨床上尚無驗證。

**若要推進需要：**
- 補齊 Avibactam 的作用機轉資料與香港仿單的警語、禁忌症
- 進行 Avibactam 搭配 β-內醯胺類藥物對結核分枝桿菌（含 BlaC）的體外與動物模型研究
- 系統性檢索泌尿生殖道結核的相關臨床與文獻資料
- 確認可行的搭配藥物與給藥途徑

---

### 附註：其他預測適應症

資料中另有三項預測，均為 L5、建議 Hold，且沒有臨床試驗或文獻支持：

| 預測適應症 | TxGNN 分數 | 說明 |
|-----------|-----------|------|
| 泌尿道血吸蟲病 (urinary schistosomiasis) | 0.9906 | 血吸蟲為寄生蟲，Avibactam 作用於細菌 β-內醯胺酶，無合理的直接抗寄生蟲機轉；此分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，並非生物學證據。標準治療為 praziquantel。 |
| 高澱粉酶血症 (hyperamylasemia) | 0.9901 | 屬實驗室檢驗異常而非感染，Avibactam 無已知降低澱粉酶的機轉；此分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，並非生物學證據。 |
| 多株性高黏滯症候群 (polyclonal hyperviscosity syndrome) | 0.9901 | Avibactam 對免疫球蛋白生成或血液流變學無已知作用，分數與高澱粉酶血症相同，疑為非特異性模型輸出。 |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

