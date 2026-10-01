---
layout: default
title: Eplerenone
parent: 僅模型預測 (L5)
nav_order: 324
evidence_level: L5
indication_count: 5
---

# Eplerenone
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

# Eplerenone：從原適應症（資料未登載）到缺氧或肺疾病所致肺動脈高壓

## 一句話總結

Eplerenone（DrugBank：DB00700）已在香港上市，但本次資料未登載其核准適應症。
TxGNN 模型預測它可能對**缺氧或肺疾病所致肺動脈高壓 (Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia)** 有效。
目前有 **0 個臨床試驗**，檢索到的 20 篇文獻談的都是一般缺氧生物學，**沒有任何一篇直接研究 eplerenone**，所以這仍只是模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 缺氧或肺疾病所致肺動脈高壓 |
| TxGNN 預測分數 | 99.50% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位是空的）。以下推論來自一般背景知識，不是本次資料的內容，尚未經證實。Eplerenone 屬於鹽皮質素受體 (MR) 拮抗劑。MR 訊號在理論上可能與肺血管重塑和纖維化有關，這是模型預測的可能路徑。

不過，缺氧造成的肺血管收縮是另一條不同的路徑，資料中沒有顯示 eplerenone 與這條路徑有直接關聯。0.995 的高分只代表模型在知識圖譜上判斷兩者相近，不等於有實證支持。

另有一個預測是「機轉不明的多因子肺動脈高壓」，分數與本項完全相同 (0.995)，很可能是同一預測的重複項目。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

檢索到 20 篇文獻，關鍵字是「缺氧 (hypoxia)」。內容涵蓋腦部、腫瘤、纖維化等一般缺氧議題，**沒有 eplerenone，也沒有肺動脈高壓的治療研究**，相關性標記均為待確認。以下列出其中 10 篇。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Res Rev | 缺氧與腦老化：缺氧可能致病，也可能有保護作用 |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metab Brain Dis | 缺氧造成認知功能受損的臨床證據與分子機轉 |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | J Cell Biochem | 缺氧對細胞代謝、血管新生等的調控 |
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review | Respir Care Clin N Am | 低血氧的四種基本機轉（此篇與肺部最接近，但未涉及藥物） |
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Review | Redox Biol | 缺氧與多發性硬化症病理及症狀的關係 |
| [40815459](https://pubmed.ncbi.nlm.nih.gov/40815459/) | 2025 | 未分類 | Rev Med Inst Mex Seguro Soc | 高海拔低氧與居民的適應性變化 |
| [33278780](https://pubmed.ncbi.nlm.nih.gov/33278780/) | 2021 | 前臨床 | Redox Biol | 缺氧下瘢痕疙瘩纖維母細胞的糖代謝改變 |
| [37328448](https://pubmed.ncbi.nlm.nih.gov/37328448/) | 2023 | 前臨床 | Adv Sci | 胃癌細胞透過 NAT10/HIF-1α 迴路增強缺氧耐受 |
| [27423661](https://pubmed.ncbi.nlm.nih.gov/27423661/) | 2016 | 未分類 | Cell Tissue Res | 缺氧在組織修復與纖維化中的角色 |
| [31961750](https://pubmed.ncbi.nlm.nih.gov/31961750/) | 2020 | 未分類 | Annu Rev Immunol | 缺氧與先天免疫、發炎反應 |

## 香港上市資訊

共 8 張許可證，以下列出 5 張。資料中未提供劑型與核准適應症，請查閱衛生署原廠仿單。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-67564 | EPLERENONA PENTAFARMA TABLETS 50MG | TRENTON-BOMA LTD |
| HK-53031 | INSPRA TAB 25MG | VIATRIS HEALTHCARE HONG KONG LIMITED |
| HK-66394 | EPEFLO 25 TABLETS 25MG | JACOBSON MARKETING LIMITED |
| HK-53030 | INSPRA TAB 50MG | VIATRIS HEALTHCARE HONG KONG LIMITED |
| HK-67701 | EPLERENONE TABLETS 50MG | HONG KONG MEDICAL SUPPLIES LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

補充說明：模型的預測理由中提到，MR 拮抗劑用於腎功能不全的患者時，須留意高血鉀風險。這是背景知識，不是仿單資料。

## 結論與下一步

**決策：Hold**

**理由：**
- 只有模型預測（L5），沒有臨床試驗，文獻也沒有一篇直接研究 eplerenone。
- 作用機轉與仿單警語資料都缺失，無法進入安全性篩選。

**若要推進需要：**
- 下載並解析衛生署仿單，補齊警語、禁忌症與核准適應症。
- 補上 DrugBank 的作用機轉 (MOA) 資料。
- 針對「eplerenone + 肺動脈高壓」做專門的文獻檢索，取代目前的泛缺氧檢索。
- 合併重複的肺動脈高壓預測項目。
- 其餘三個預測：惡性高血壓腎病與惡性腎血管性高血壓可列為研究問題，須先評估高血鉀與腎功能風險；Braddock syndrome 可能只是圖譜相近造成的假訊號。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

