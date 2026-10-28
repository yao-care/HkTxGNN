---
layout: default
title: Spectinomycin
parent: 僅模型預測 (L5)
nav_order: 831
evidence_level: L5
indication_count: 10
monitor_inn: "SPECTINOMYCIN"
predicted_indications: ["disease of uterine broad ligament", "abdominal ectopic pregnancy", "celiac trunk compression syndrome", "abdominal cystic lymphangioma", "lymph node palisaded myofibroblastoma", "disease of retroperitoneum", "sacrum chordoma", "urethral disease", "disease of peritoneum", "embryonic cyst of fallopian tube"]
last_modified_at: 2026-10-28
description: "Spectinomycin：預測新適應症為子宮闊韌帶疾病（證據等級 L5）。原適應症：急性淋球菌性子宮頸炎、淋病"
---

# Spectinomycin
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

## Spectinomycin：從淋病到子宮闊韌帶疾病
{: .text-alpha }

## 一句話總結

Spectinomycin 是一種胺基環醇類抗生素，知識圖譜中記錄的原適應症為急性淋球菌性子宮頸炎與淋病。
TxGNN 模型預測它可能對**子宮闊韌帶疾病 (disease of uterine broad ligament)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持，僅為模型預測，屬於 L5 證據等級。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 急性淋球菌性子宮頸炎、淋病（知識圖譜中記錄的關聯；香港許可證資料未載明適應症文字） |
| 預測新適應症 | 子宮闊韌帶疾病 |
| TxGNN 預測分數 | 0.9957 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知資訊，spectinomycin 屬胺基環醇類抗生素，作用於細菌 30S 核糖體以抑制蛋白質合成，對淋病奈瑟菌有抗菌活性。

子宮闊韌帶疾病若與骨盆腔細菌感染有關，理論上或可與抗菌作用產生連結，但本次整理的資料中沒有任何證據支持這一點。此預測分數雖高（0.9957），但來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，並非生物學證據，且排名偏後（第 8012 名），不能視為療效訊號。

另外值得注意的是，排名第 1 至第 7 的預測（例如異位妊娠、腹腔囊性淋巴管瘤、骶骨脊索瘤等）多為非感染性疾病，與抗菌機轉明顯不符，顯示這批預測的可信度有限。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

**補充說明（其他預測項目）：** 排名第 8 的「尿道疾病」有較多文獻（約 20 篇），內容主要是淋菌性尿道炎的治療，與原適應症高度重疊，並非真正的新適應症。其中 2025 年一篇報告指出，肌肉注射 spectinomycin 對 4 例難治性生殖道黴漿菌 (Mycoplasma genitalium) 尿道炎有效，是較新穎的訊號，但屬小規模觀察性報告。排名第 9 的「腹膜疾病」僅有 1 篇 1979 年關於淋球菌性骨盆腔炎處置的文章，屬間接證據。這些都不直接針對本報告的主要預測疾病。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-35734 | KIRIN INJ 2G | 未載明 | 未載明 |
| HK-54939 | MICOSPECTONE INJECTABLE SOLUTION (VET) | 未載明 | 未載明 |
| HK-36853 | KIRIN INJ 2G WITH DILUENT | 未載明 | 未載明 |

其中 HK-54939 的品名標示為獸用 (VET)，與人用藥品性質不同，解讀時需留意。

## 安全性考量

- **藥物交互作用**：資料庫共記錄 1 筆，與 Picosulfuric acid 的交互作用等級為中度。

其餘安全性資訊（警語、禁忌症）請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測的主要疾病（子宮闊韌帶疾病）沒有任何臨床試驗或文獻，僅有模型分數，且機轉上缺乏合理連結，證據等級為 L5。
- 香港許可證資料中缺少適應症文字與仿單安全性資訊，目前無法進行安全性篩選。

**若要推進需要：**
- 取得 spectinomycin 的作用機轉資料與香港仿單（警語、禁忌症、核准適應症）
- 釐清子宮闊韌帶疾病中是否存在可由 spectinomycin 敏感菌引起的感染型態，並進行文獻回顧
- 若欲探索較有前景的方向，可優先評估難治性黴漿菌 (Mycoplasma genitalium) 尿道炎，但需有更嚴謹設計的研究支持
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

