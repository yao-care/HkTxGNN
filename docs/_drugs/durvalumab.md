---
layout: default
title: Durvalumab
parent: 僅模型預測 (L5)
nav_order: 304
evidence_level: L5
indication_count: 6
monitor_inn: "Durvalumab"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
last_modified_at: 2026-10-23
description: "Durvalumab：預測新適應症為子宮韌帶腺癌（證據等級 L5）。原適應症：移行細胞癌"
---

# Durvalumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

## Durvalumab：從移行細胞癌到子宮韌帶腺癌
{: .text-alpha }

## 一句話總結

Durvalumab 是一種 PD-L1 抑制劑，知識圖譜記錄its 與**移行細胞癌**有關聯。
TxGNN 模型預測它可能對**子宮韌帶腺癌**有效，但目前**沒有臨床試驗或文獻**直接支持這個方向，只有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 移行細胞癌（知識圖譜記錄的關聯；香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 子宮韌帶腺癌 |
| TxGNN 預測分數 | 0.9992 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Durvalumab 屬於 PD-L1 抑制劑，一般認為其作用是阻斷 PD-L1 訊號，讓 T 細胞恢復對腫瘤的攻擊能力。

理論上，若子宮韌帶腺癌這類婦科腺癌表現 PD-L1，或腫瘤突變負荷較高，檢查點抑制劑可能有效。不過這只是推測，現有資料中沒有任何試驗或文獻支持。0.9992 的分數僅代表模型預測，不等於臨床療效。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65929 | IMFINZI CONCENTRATE FOR SOLUTION FOR INFUSION 500MG/10ML | 未載明 | 未載明 |
| HK-65928 | IMFINZI CONCENTRATE FOR SOLUTION FOR INFUSION 120MG/2.4ML | 未載明 | 未載明 |

兩張皆為單一成分製劑，持證商為 ASTRAZENECA HONG KONG LIMITED，狀態有效。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 免疫治療（免疫檢查點抑制劑），非傳統細胞毒性藥物 |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：資料庫共記錄 81 項交互作用，以下為部分項目。
  - 重大等級：Adalimumab。
  - 中等等級：多種皮質類固醇（Hydrocortisone、Dexamethasone、Prednisone、Methylprednisolone 等）、Roflumilast、Deflazacort、Alemtuzumab、Anakinra、破傷風類毒素疫苗及炭疽疫苗等。
  - 輕微等級：多種鋅製劑。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這項預測目前沒有任何臨床試驗或文獻直接支持，證據等級為 L5，只憑模型分數不足以推進。
- 香港許可證資料也未提供核准適應症文字，且作用機轉資料缺漏。

**若要推進需要：**
- 取得香港仿單，確認核准適應症、警語與禁忌症。
- 補齊作用機轉資料。
- 檢索子宮韌帶腺癌的 PD-L1 表現及免疫治療反應相關研究。
- 若有相關試驗或文獻，再重新評估證據等級。

**補充觀察：** 排名第 2 的「子宮頸管癌」有一項已完成的 Phase 1 試驗（[NCT03452332](https://clinicaltrials.gov/study/NCT03452332)，n=20，放射治療合併 durvalumab 與 tremelimumab）。但它針對的是另一種疾病，不能用來支持本報告的主要預測，若要優先探索婦科腫瘤方向，可考慮另案評估。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

