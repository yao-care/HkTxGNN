---
layout: default
title: Midecamycin
parent: 僅模型預測 (L5)
nav_order: 497
evidence_level: L5
indication_count: 10
---

# Midecamycin
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

# Midecamycin：從細菌感染到念珠菌病（Candidiasis）

## 一句話總結

> Midecamycin 是一種巨環內酯類（macrolide）抗生素，作用機轉為抑制細菌 50S 核糖體蛋白合成，原用於治療細菌感染，但目前查無其在香港上市的正式適應症資料。
> TxGNN 模型預測分數最高的新方向是**念珠菌病 (Candidiasis)**，惟臨床試驗與文獻證據均為 **0 筆**，且模型本身的機轉合理性評估指出此預測可能是知識圖譜雜訊，而非真實藥理關聯。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（無許可證/仿單資料，僅知屬巨環內酯類抗生素） |
| 預測新適應症 | 念珠菌病 (Candidiasis) |
| TxGNN 預測分數 | 99.02% |
| 證據等級 | L5（僅模型預測，無臨床試驗或文獻） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Midecamycin 詳細的作用機轉資料（`original_moa` 為資料缺口）。根據 Evidence Pack 提供的機轉推論，Midecamycin 屬於巨環內酯類抗生素，藥理標的是細菌 50S 核糖體，用以抑制蛋白質合成。

**就念珠菌病（本次分數最高的預測）而言，機轉上並不合理**：Candidiasis 是由念珠菌（真菌）引起的感染，而 Midecamycin 的藥理標的是細菌核糖體，對真菌無已知活性。Evidence Pack 中的機轉分析也直接指出，這個高分很可能是知識圖譜中「共現/間接節點」造成的雜訊，而非真實的藥理關聯。

在同一份預測清單中，**痲瘋病 (Leprosy，排名第 2）機轉上反而更具合理性**：同為巨環內酯類的 clarithromycin 已知對 *Mycobacterium leprae* 具有體外/臨床活性、並曾用於多重藥物治療方案；Midecamycin 屬同類藥物，理論上可能有類似效應，但目前完全沒有針對 Midecamycin 本身的實證資料。整體而言，這批預測目前僅停留在模型分數層次，尚未有實證支持任一方向。

---

## 臨床試驗證據

目前無相關臨床試驗登記（Candidiasis 及其餘 9 個預測適應症皆查無 ClinicalTrials.gov / ICTRP 登記試驗）。

---

## 文獻證據

目前無相關文獻（PubMed 查詢 Midecamycin + Candidiasis 結果為 0 筆，其餘 9 個預測適應症亦同）。

---

## 香港上市資訊

Midecamycin 目前**未在香港上市**，查無任何許可證登記資料。

---

## 全部預測適應症一覽

本次 Evidence Pack 共列出 10 個 TxGNN 預測適應症，皆為 L5 等級（僅模型預測、無實證），整理如下供參考：

| 排名 | 預測適應症 | TxGNN 分數 | 決策階段 | 建議 |
|------|-----------|-----------|---------|------|
| 1 | Candidiasis（念珠菌病） | 99.02% | S0 | Hold |
| 2 | Leprosy（痲瘋病） | 98.95% | S1 | Research Question |
| 3 | Coronary artery disease（冠狀動脈疾病） | 98.70% | S0 | Hold |
| 4 | Myocardial ischemia（心肌缺血） | 98.53% | S0 | Hold |
| 5 | ALCAPA（左冠狀動脈異常起源） | 98.40% | S0 | Hold |
| 6 | Pneumocystosis（肺囊蟲病） | 98.28% | S0 | Hold |
| 7 | Polyp of vocal cord（聲帶息肉） | 98.23% | S0 | Hold |
| 8 | Uterine polyp（子宮息肉） | 98.22% | S0 | Hold |
| 9 | Polyp of middle ear（中耳息肉） | 98.22% | S0 | Hold |
| 10 | Polyp of frontal sinus（額竇息肉） | 98.19% | S1 | Research Question |

值得注意：第 3、4 名（冠心病、心肌缺血）背後的「巨環內酯抗發炎假說」已被同類藥物大型 RCT（WIZARD、CLARICOR）否定，CLARICOR 甚至觀察到死亡率上升訊號，屬已知的負向類別效應，不建議探索。

---

## 安全性考量

安全性資訊請參考原廠仿單。（TFDA/香港仿單警語、禁忌症、藥物交互作用查詢均無結果，屬待補資料，見下方阻斷性缺口。）

---

## 結論與下一步

**決策：Hold**

**理由：**
- 分數最高的預測（Candidiasis）機轉上不成立，Evidence Pack 自身分析已判定其為知識圖譜雜訊。
- 全部 10 個預測適應症皆為 L5 等級，無任何臨床試驗或文獻實證支持。
- 存在一項**阻斷性（Blocking）資料缺口**：TFDA/仿單警語與禁忌症未取得，無法進入安全性初評（S1）。

**若要推進需要：**
- 取得 Midecamycin 完整仿單（警語、禁忌症、DDI），解除阻斷性資料缺口
- 補齊作用機轉（MOA）詳細資料，供機轉關聯性分析使用
- 若要延續研究方向，優先鎖定機轉上較合理的 Leprosy（排名 2）與 Polyp of frontal sinus（排名 10，屬巨環內酯類已知的免疫調節/抗發炎類別效應），而非目前分數最高但機轉不成立的 Candidiasis
- 針對 Leprosy 方向，檢索同類藥物（clarithromycin）在痲瘋病治療的實證資料，評估類別效應延伸至 Midecamycin 的合理性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

