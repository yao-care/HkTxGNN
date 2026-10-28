---
layout: default
title: Fosfomycin
parent: 僅模型預測 (L5)
nav_order: 401
evidence_level: L5
indication_count: 8
monitor_inn: "FOSFOMYCIN"
predicted_indications: ["uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "epiglottitis", "urogenital tuberculosis", "laryngitis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "pyelitis"]
last_modified_at: 2026-10-23
description: "Fosfomycin：預測新適應症為Uterine inflammatory disease（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Fosfomycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

## Fosfomycin: Uterine inflammatory disease
{: .text-alpha }

## 一句話總結

Fosfomycin（磷黴素）是廣效殺菌性抗生素，在知識圖譜中記錄的原適應症為尿路感染。
TxGNN 模型預測它可能對**子宮發炎性疾病**有效，但目前沒有直接研究這個疾病的臨床試驗或文獻，證據僅停留在**模型預測**層級。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Uterine inflammatory disease |
| TxGNN 預測分數 | 0.9998 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Fosfomycin 抑制細菌 MurA 酶（UDP-N-乙醯葡萄糖胺烯醇丙酮酸轉移酶），阻斷細菌細胞壁合成的早期步驟。它對多種易感菌有活性，且在尿液中濃度很高。

從機轉看，若子宮發炎由易感菌引起，抗菌藥物理論上可能有作用。尿路與骨盆腔、生殖道的感染在病原菌上有部分重疊，這可能是模型給出高分的原因。

不過，本次整理的資料中沒有任何直接證據：
- 兩個臨床試驗都是兒童「未充分研究藥物」的一般藥動學研究，並未檢驗子宮發炎。
- 唯一的文獻談的是 dienogest 相關膀胱炎，屬於泌尿道問題，並非子宮發炎。

因此這個預測目前只是假說。

> 附註：同一份預測清單中的「腎盂炎 (pyelitis)」與原適應症最接近，且有 ZEUS 研究（靜脈注射 fosfomycin 對比 piperacillin-tazobactam 治療複雜性尿路感染，含急性腎盂腎炎）等文獻。若要挑選優先研究方向，該適應症比子宮發炎性疾病更值得先評估。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | 不適用 | 完成 | 3520 | 兒童依常規照護使用「未充分研究藥物」的藥動學研究，並未針對子宮發炎提出療效問題 |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | 不適用 | 招募中 | 5000 | 兒童與年輕成人未充分研究藥物的藥動學、藥效學與安全性研究，屬通用型平台試驗，與本適應症無直接關係 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35653789](https://pubmed.ncbi.nlm.nih.gov/35653789/) | 2022 | 世代研究 | Journal of Obstetrics and Gynaecology | 探討子宮內膜異位症女性術後使用 dienogest 與複方口服避孕藥時的膀胱炎症狀與菌尿；屬泌尿道議題，與 fosfomycin 治療子宮發炎無直接關聯 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-43159 | MONUROL SACHETS 3G | 未提供 | 未提供 |

此許可證為單一成分製劑，狀態有效，持有者為 ZENFIELDS (H.K.) LIMITED。

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單文字）：腎臟疾病、輸尿管積膿、困難梭狀芽孢桿菌結腸炎、新生兒壞死性腸炎。
- **藥物交互作用**（共 3 項）：
  - Balsalazide：中度
  - Picosulfuric acid：中度
  - Metoclopramide：輕度

其餘安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗或文獻直接研究 fosfomycin 用於子宮發炎性疾病，現有兩個試驗與一篇文獻都只是間接相關，因此證據等級為 L5。
- 機轉上雖有合理性，但缺乏臨床證據，不宜推進。

**若要推進需要：**
- 確認子宮發炎的常見病原菌對 fosfomycin 的敏感性，以及藥物在子宮與骨盆腔組織的穿透濃度。
- 搜尋並評估 fosfomycin 用於婦產科感染（如產後子宮內膜炎、骨盆腔發炎）的直接研究。
- 取得原廠仿單中的核准適應症、警語與禁忌資料。
- 考慮改以證據較強的「腎盂炎」為優先評估對象，並確認 ZEUS 研究的試驗階段分類。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

