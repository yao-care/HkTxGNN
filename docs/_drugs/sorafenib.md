---
layout: default
title: Sorafenib
parent: 僅模型預測 (L5)
nav_order: 812
evidence_level: L5
indication_count: 5
---

# Sorafenib
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

# Sorafenib：從（原適應症資料缺漏）到脂肪肉瘤

## 一句話總結

Sorafenib 是一種口服多重激酶抑制劑，在香港已有 6 張許可證上市，但本資料包未提供原適應症文字。
TxGNN 模型預測它可能對**脂肪肉瘤 (Liposarcoma)** 有效，
目前有 **2 個相關臨床試驗**和 **8 篇文獻**，但都不是脂肪肉瘤專屬的直接證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 脂肪肉瘤 (Liposarcoma) |
| TxGNN 預測分數 | 99.82% |
| 證據等級 | L2（依資料包評定；實際僅有混合組織型軟組織肉瘤的 Phase 2 資料，偏間接） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Hold（列為研究問題） |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據一般藥理知識，Sorafenib 是多重激酶抑制劑，作用於 RAF/MEK/ERK 路徑，以及 VEGFR、PDGFR 等血管新生相關受體。這段機轉是依一般知識推論，並非來自本次提供的資料。

這些路徑在軟組織肉瘤的血管新生與細胞訊息傳遞中可能扮演角色。另有去分化脂肪肉瘤異種移植模型研究顯示 PTEN/PI3K-AKT 路徑可能參與。

但 Sorafenib 在肉瘤中的活性似乎取決於組織型，本資料中沒有脂肪肉瘤專屬的療效證據。TxGNN 分數（0.998）只是模型預測，不能取代臨床證據。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | 完成 | 51 | 以 Sorafenib（BAY 43-9006）治療晚期軟組織肉瘤；混合組織型，無法單獨看脂肪肉瘤結果（相關性 B） |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | 完成 | 131 | SARC024：測試的是 Regorafenib（Sorafenib 的結構類似物），並非 Sorafenib，僅屬類別層級的間接支持（相關性 C） |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | Phase 2 試驗（單臂） | Cancer | SWOG S0505：Sorafenib 用於晚期軟組織肉瘤 |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Phase 1 試驗 | Ann Surg Oncol | 術前適形放療併用 Sorafenib，用於局部晚期肢體軟組織肉瘤 |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Ann Oncol | 軟組織肉瘤依組織型的治療；Trabectedin 對脂肪肉瘤有活性 |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar Onkologia | 依組織型的軟組織肉瘤藥物治療（匈牙利文） |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Front Oncol | 肉瘤 PDOX 小鼠模型與 Palbociclib 組合療法 |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | 前臨床 | Mol Cancer Ther | Sorafenib 抑制惡性周邊神經鞘瘤細胞生長與 MAPK 訊號；所用細胞株含去分化脂肪肉瘤株 |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | 前臨床 | Am J Pathol | 去分化脂肪肉瘤異種移植模型，顯示 PTEN 下調與對 PI3K 路徑抑制的反應 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 廠商 |
|---------|------|------|------|
| HK-55409 | NEXAVAR TAB 200MG | 未提供 | BAYER HEALTHCARE LIMITED |
| HK-67562 | SORAFENIB STADA TABLETS 200MG | 未提供 | STADA PHARMACEUTICALS (ASIA) LIMITED |
| HK-66345 | SORAFENAT TABLETS 200MG | 未提供 | I & C (HONG KONG) LIMITED |
| HK-68075 | RAFALVO TABLETS 200MG | 未提供 | LOTUS PHARMACEUTICAL HK LIMITED |
| HK-68600 | SORAFENIB TABLETS USP 200MG | 未提供 | CHEMILL PHARMA LIMITED |

資料包另載明共 6 張許可證，此處僅列出提供的 5 張。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（多重激酶抑制劑） |

其餘項目（骨髓抑制風險、致吐性、監測項目、處置防護）本資料包沒有提供，請參考原廠仿單的警語與注意事項。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 唯一直接測試 Sorafenib 的軟組織肉瘤試驗是混合組織型的 Phase 2，無法判斷脂肪肉瘤是否受益；其他證據多為前臨床或間接資料。
- 香港仿單的警語與禁忌資料尚缺，無法進入安全性篩選。

**若要推進需要：**
- 取得 SWOG S0505（PMID 21751200）與 NCT00217620 的脂肪肉瘤亞組結果
- 從香港衛生署下載並解析仿單，補齊警語與禁忌症
- 從 DrugBank 補充作用機轉資料
- 補充原適應症資料（許可證的核准適應症文字目前為空）

---

### 其他預測適應症（供參考）

| 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|-----------|-----------|---------|------|
| 未分類腎細胞癌 (Unclassified RCC) | 99.65% | L4 | 研究問題。有 Phase 3 試驗 [NCT01613846](https://clinicaltrials.gov/study/NCT01613846)（Sorafenib 與 Pazopanib 序貫比較，n=544），但為一般晚期腎細胞癌族群，對此亞型屬間接證據 |
| 卵巢黏液樣脂肪肉瘤 | 99.76% | L5 | Hold，僅有模型預測 |
| Xp11.2 轉位/TFE3 融合相關腎細胞癌 | 99.65% | L5 | Hold，僅有模型預測 |
| 腎細胞癌合併神經母細胞瘤 | 99.65% | L5 | Hold，僅有模型預測 |

本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

