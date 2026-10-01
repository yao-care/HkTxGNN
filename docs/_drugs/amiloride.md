---
layout: default
title: Amiloride
parent: 僅模型預測 (L5)
nav_order: 48
evidence_level: L5
indication_count: 6
---

# Amiloride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Amiloride：從保鉀利尿劑到惡性高血壓腎病變

## 一句話總結

Amiloride 是一種保鉀利尿劑，作用在上皮鈉通道（ENaC）。
TxGNN 模型預測它可能對**惡性高血壓腎病變 (Malignant Hypertensive Renal Disease)** 有效。
目前**沒有臨床試驗，也沒有直接相關的文獻**，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 惡性高血壓腎病變 (Malignant Hypertensive Renal Disease) |
| TxGNN 預測分數 | 99.82% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

香港許可證資料未載明核准適應症，因此本報告不列原適應症。

## 為什麼這個預測合理？

Amiloride 阻斷上皮鈉通道（ENaC），減少腎臟的鈉再吸收並保留鉀離子。從血壓與鈉水平衡的角度看，用於高血壓相關腎臟疾病在機轉上有合理性。

不過，目前缺乏詳細的作用機轉資料，也沒有任何臨床試驗或文獻直接檢驗 amiloride 對惡性高血壓腎病變的效果。這個預測目前只能視為假說，尚無實證支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 其他預測適應症（供參考）

| 預測適應症 | 分數 | 證據等級 | 說明 |
|-----------|------|---------|------|
| 惡性腎血管性高血壓 | 99.82% | L4 | 僅有 2003 年一篇談礦皮質素高血壓檢查的綜述（PMID [12929904](https://pubmed.ncbi.nlm.nih.gov/12929904/)），屬間接證據，未顯示 amiloride 的臨床效益 |
| 機轉不明的多因素肺高壓 | 99.81% | L5 | 僅有模型預測 |
| 肺疾病／缺氧所致肺高壓 | 99.81% | L5 | 檢索到的文獻是一般缺氧主題，並未研究 amiloride，視為關鍵字比對雜訊，不計為證據 |
| Braddock 症候群 | 99.75% | L5 | 僅有模型預測 |
| 慢性肺心病 | 99.68% | L4 | 有心衰竭族群的間接證據（見下方） |

**慢性肺心病**是其中證據最多的一項，但仍屬間接證據：
- [PMID 1888694](https://pubmed.ncbi.nlm.nih.gov/1888694/)（1991）：雙盲交叉試驗，慢性心衰竭且服用 digoxin 的病人加上 amiloride，血行動力學有改善。
- [PMID 2888942](https://pubmed.ncbi.nlm.nih.gov/2888942/)（1987）：雙盲交叉試驗，比較 captopril 單用與 furosemide 加 amiloride 治療輕度心衰竭。
- [PMID 16815890](https://pubmed.ncbi.nlm.nih.gov/16815890/)（2006）：大鼠研究，代償性心衰竭時肺泡液體再吸收增加，支持 ENaC 相關的肺部機轉。

這些研究的族群是心衰竭，不是肺心病，且沒有登記中的相關試驗。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-25543 | AMILORIDE TAB 5MG | JEAN-MARIE PHARMACAL CO LTD |
| HK-25544 | AMITHIAZIDE TAB | JEAN-MARIE PHARMACAL CO LTD |
| HK-42186 | APO-AMILZIDE TAB 50/5MG | HIND WING CO LTD |
| HK-50535 | POLI-URETIC TAB | NATURAL HEALTH RESOURCES COMPANY LIMITED |
| HK-58537 | BILDURETIC TAB | TRENTON-BOMA LTD |

## 安全性考量

安全性資訊請參考原廠仿單。藥物交互作用查詢無結果。

有一則值得留意的線索：一篇病例報告（[PMID 8615380](https://pubmed.ncbi.nlm.nih.gov/8615380/)）描述一位 96 歲病人在使用 trimethoprim-sulfamethoxazole 後出現嚴重高血鉀。該案例用的不是 amiloride，但保鉀類藥物同樣有高血鉀風險，尤其在老年人或腎功能不全者。

## 結論與下一步

**決策：Hold**

**理由：**
- 首要預測適應症只有 TxGNN 模型分數，沒有任何臨床試驗或直接文獻支持。
- 香港仿單的警語與禁忌症資料尚未取得，安全性篩選無法進行。

**若要推進需要：**
- 取得香港衞生署核准的仿單，確認警語、禁忌症與核准適應症。
- 補充 DrugBank 的作用機轉資料。
- 針對「amiloride ＋ 惡性高血壓／高血壓腎病變」做專門的文獻檢索，排除關鍵字比對雜訊。
- 評估更有間接證據的方向（如慢性肺心病）是否值得優先研究，並納入高血鉀與腎功能監測計畫。

> 本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

