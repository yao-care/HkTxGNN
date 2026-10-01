---
layout: default
title: Valine
parent: 中證據等級 (L3-L4)
nav_order: 907
evidence_level: L4
indication_count: 10
---

# Valine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Valine：從胺基酸營養補充到硬化性膽管炎

## 一句話總結

Valine（纈胺酸）是一種支鏈胺基酸（BCAA），在香港以胺基酸輸液與顆粒製劑上市。
TxGNN 模型預測它可能對**硬化性膽管炎 (Sclerosing Cholangitis)** 有效，但目前**沒有臨床試驗**，只有 **2 篇間接相關文獻**，且都沒有測試補充 Valine 的效果。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明適應症文字 |
| 預測新適應症 | 硬化性膽管炎 (Sclerosing Cholangitis) |
| TxGNN 預測分數 | 99.42% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Valine 是支鏈胺基酸（BCAA），常見於複方胺基酸製劑，是人體必需的營養成分。

膽汁淤積性肝病（包括原發性膽汁性膽管炎 PBC 與硬化性膽管炎 PSC）的患者，已有研究描述其血中胺基酸組成異常，例如 BCAA 與芳香族胺基酸失衡。這是模型預測合理的間接線索。

但這只是代謝層面的關聯。現有文獻探討的是血漿酪胺酸與疲勞的關係，以及血中代謝物與疾病風險的因果關聯，沒有任何一篇測試給予 Valine 能否改善疾病。要說 Valine 具有治療效果，目前沒有機轉層面的證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39015781](https://pubmed.ncbi.nlm.nih.gov/39015781/) | 2024 | Mendelian randomization | Frontiers in medicine | 以孟德爾隨機化分析血中代謝物與 PBC、PSC 風險的因果關係，屬代謝物層級的關聯，未測試 Valine 給藥 |
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Cohort | BMC gastroenterology | 探討 PBC 與 PSC 患者血漿酪胺酸濃度與疲勞的關係，主題是酪胺酸，不是 Valine 治療 |

## 香港上市資訊

香港共有 20 張相關許可證，以下列出 5 張。許可證資料未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-62890 | LIVACT GRANULES | EISAI (HONG KONG) COMPANY LIMITED |
| HK-57540 | AMINOL-S INJ | WINGS PHARMACEUTICAL LTD |
| HK-62100 | AMINOGEN-S SOLUTION FOR INFUSION | WINGS PHARMACEUTICAL LTD |
| HK-60459 | PAN-VASOL SOLUTION FOR INJECTION | FALKAN MEDICAL LIMITED |
| HK-58914 | PAN-AMIN G INJ | OTSUKA PHARMACEUTICAL (H.K.) LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 分數很高，但沒有臨床試驗，現有 2 篇文獻只顯示代謝關聯，沒有測試 Valine 的治療效果。
- 香港仿單的警語與禁忌資料也還沒取得，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單，完成警語與禁忌症資料（目前為阻斷性缺口）
- 補齊 Valine 的作用機轉資料（DrugBank）
- 針對 BCAA／Valine 補充用於 PSC 或膽汁淤積性肝病，做專門的文獻檢索
- 釐清 BCAA 失衡究竟是疾病的原因還是結果，再評估補充是否有益

**其他預測適應症：**
排名後面的預測多半只有模型分數，或文獻只是因「Val」出現在基因變異名稱而被檢索到，與 Valine 作為藥物無關。這些預測同樣建議 Hold。

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

