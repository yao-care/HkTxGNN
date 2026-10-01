---
layout: default
title: Tetracaine
parent: 僅模型預測 (L5)
nav_order: 852
evidence_level: L5
indication_count: 5
---

# Tetracaine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Tetracaine：從局部麻醉到慢性萎縮性肢端皮膚炎

## 一句話總結

Tetracaine 是酯類局部麻醉藥，在香港有眼藥水與外用乳膏兩種製劑上市。
TxGNN 模型預測它可能對**慢性萎縮性肢端皮膚炎 (Acrodermatitis Chronica Atrophicans)** 有效。
目前**沒有任何臨床試驗或文獻**支持這個預測，僅有模型分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 慢性萎縮性肢端皮膚炎 (Acrodermatitis Chronica Atrophicans) |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Tetracaine 屬於酯類局部麻醉藥，一般認為是透過阻斷電壓門控鈉離子通道產生局部麻醉作用。這是依藥物類別推論，並非來自 DrugBank 的 MOA 資料。

慢性萎縮性肢端皮膚炎是伯氏疏螺旋體 (Borrelia) 感染後期的皮膚表現。Tetracaine 沒有已知的抗菌或抗萎縮作用，兩者之間找不到合理的機轉關聯。

TxGNN 分數很高 (99.93%)，但這只是模型輸出，沒有臨床或文獻佐證。以現有資料來看，這個預測較可能是模型的假陽性，不宜當作有效的老藥新用訊號。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-54171 | MINIMS TETRACAINE HYDROCHLORIDE EYE DROPS 1% (LAB CHAUVIN) | BAUSCH & LOMB (HK) LTD |
| HK-63840 | PLIAGLIS CREAM | PROFESSIONAL QUALITY & REGULATORY RESOURCES LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測只有模型分數，沒有任何臨床試驗或文獻支持，證據等級為 L5。
- 藥物機轉與疾病病因（螺旋體感染）沒有合理連結。
- 其他排名較後的預測適應症也沒有直接的治療證據：
  - 痤瘡瘢痕疙瘩 (acne keloid) 有一個 Phase 4 試驗 (NCT02372786) 與一篇文獻 (PMID 27377616)，但兩者研究的都是雷射治療時的**局部麻醉止痛效果**，並非治療疾病本身。
  - 支氣管炎 (bronchitis) 僅有一篇 1988 年文獻，從標題看不出有測試 tetracaine。

**若要推進需要：**
- 補齊 DrugBank 作用機轉資料。
- 取得香港衛生署的仿單，確認警語與禁忌症。
- 除非有新的機轉或臨床證據，否則不建議投入資源。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

