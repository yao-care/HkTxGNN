---
layout: default
title: Daunorubicin
parent: 僅模型預測 (L5)
nav_order: 244
evidence_level: L5
indication_count: 10
---

# Daunorubicin
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

# Daunorubicin：從蒽環類抗腫瘤藥到何杰金氏淋巴瘤

## 一句話總結

Daunorubicin 是蒽環類（anthracycline）細胞毒性藥物，香港目前有 1 張上市許可證（Pfizer 的 DAUNOBLASTINA 注射劑），但許可證未載明核准適應症。
TxGNN 模型預測它可能對**何杰金氏淋巴瘤 (Hodgkin's lymphoma)** 有效。相關的 50 個臨床試驗與 20 篇文獻幾乎都在討論同類藥物 doxorubicin，**沒有任何一項直接檢驗 daunorubicin**，因此證據屬於類別層級的間接支持。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明 |
| 預測新適應症 | 何杰金氏淋巴瘤 (Hodgkin's lymphoma) |
| TxGNN 預測分數 | 99.81%（模型排名第 4353） |
| 證據等級 | L4（類別層級與機轉推論，無 daunorubicin 直接證據） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。Daunorubicin 屬蒽環類，一般認為透過嵌入 DNA 與抑制 topoisomerase II 殺死快速增生的腫瘤細胞。

何杰金氏淋巴瘤的標準化療（ABVD、AVD、BEACOPP 等）都以蒽環類為骨幹，這是這個預測看起來合理的主要原因。不過這些方案使用的是同類藥物 **doxorubicin**，不是 daunorubicin。

目前沒有證據顯示 daunorubicin 在 doxorubicin 已是標準治療的情境下有額外好處。這個預測目前只能視為研究假說，還不是可執行的用藥建議。

## 臨床試驗證據

資料共有 50 個相關試驗，以下列出與何杰金氏淋巴瘤最相關的 10 個。**其中沒有任何一個明確使用 daunorubicin**，蒽環類皆為 doxorubicin 或 AVD/ABVD 方案。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00002561](https://clinicaltrials.gov/study/NCT00002561) | Phase 3 | 完成 | 405 | 早期何杰金氏病：放療或 ABVD 加放療 vs 單用 ABVD |
| [NCT01251107](https://clinicaltrials.gov/study/NCT01251107) | Phase 3 | 完成 | 331 | 晚期或不良預後何杰金氏淋巴瘤：ABVD vs BEACOPP，合併或不合併放療 |
| [NCT00002495](https://clinicaltrials.gov/study/NCT00002495) | Phase 3 | 完成 | 348 | I-II 期：次全淋巴結放療 vs 加上 doxorubicin 與 vinblastine |
| [NCT01868451](https://clinicaltrials.gov/study/NCT01868451) | 不適用 | 完成 | 118 | 早期不良預後：brentuximab vedotin 加 AVD，比較 4 組治療結果（蒽環類為 doxorubicin） |
| [NCT00416377](https://clinicaltrials.gov/study/NCT00416377) | 不適用 | 未知 | 353 | 年輕何杰金氏淋巴瘤患者：放療或合併化療（未載明是否含 daunorubicin） |
| [NCT04624984](https://clinicaltrials.gov/study/NCT04624984) | Phase 2 | 未知 | 42 | 復發或難治型：PD-1 抑制劑 ± GVD（含脂質體 doxorubicin） |
| [NCT02298283](https://clinicaltrials.gov/study/NCT02298283) | Phase 2 | 完成 | 40 | I/II 期、ABVD 2 週期後 PET 陽性：brentuximab vedotin 鞏固治療 |
| [NCT03226249](https://clinicaltrials.gov/study/NCT03226249) | Phase 2 | 未知 | 30 | 新診斷：PET 導向的 pembrolizumab 加 AVD |
| [NCT00654732](https://clinicaltrials.gov/study/NCT00654732) | Phase 2 | 完成 | 58 | 晚期預後不良：rituximab 加 ABVD vs 單用 ABVD |
| [NCT06831370](https://clinicaltrials.gov/study/NCT06831370) | Phase 4 | 招募中 | 124 | 印度未治療 III/IV 期：brentuximab vedotin 加 AVD 的安全性與療效 |

## 文獻證據

資料共有 20 篇文獻，以下列出 10 篇。**唯一直接涉及 daunorubicin 的是 1997 年的小型脂質體研究**，其餘皆為 doxorubicin 方案或一般性文獻。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39413375](https://pubmed.ncbi.nlm.nih.gov/39413375/) | 2024 | RCT | N Engl J Med | Nivolumab 加 AVD 用於晚期古典型何杰金氏淋巴瘤；摘要僅提供背景：brentuximab 在成人增加毒性，PD-1 阻斷在何杰金氏淋巴瘤有效 |
| [36322844](https://pubmed.ncbi.nlm.nih.gov/36322844/) | 2022 | RCT | N Engl J Med | 兒童高風險何杰金氏淋巴瘤：brentuximab vedotin 加化療；成人研究顯示療效較高但毒性也較多，兒童療效未明 |
| [35830649](https://pubmed.ncbi.nlm.nih.gov/35830649/) | 2022 | RCT | N Engl J Med | III/IV 期：A+AVD 對比 ABVD，5 年追蹤顯示長期無惡化存活優勢，並探討整體存活 |
| [9387047](https://pubmed.ncbi.nlm.nih.gov/9387047/) | 1997 | 早期臨床研究 | Invest New Drugs | 19 名復發或難治淋巴瘤患者使用脂質體 daunorubicin：低劑量無客觀反應；高劑量（9 人）有 1 例完全緩解、2 例部分緩解，未見明顯心功能惡化 |
| [20425365](https://pubmed.ncbi.nlm.nih.gov/20425365/) | 2007 | Review | Curr Hematol Malig Rep | 比較 BEACOPP 與 ABVD：ABVD 後約 20% 未達完全緩解、約 40% 長期追蹤復發 |
| [28365830](https://pubmed.ncbi.nlm.nih.gov/28365830/) | 2017 | Review | Curr Oncol Rep | 早期何杰金氏淋巴瘤在風險與反應導向策略下，放療的角色 |
| [14584273](https://pubmed.ncbi.nlm.nih.gov/14584273/) | 2003 | 回顧 | Gan To Kagaku Ryoho | 血液腫瘤總覽：daunorubicin 與 cytarabine 使急性骨髓性白血病可治癒；晚期何杰金氏淋巴瘤一線為 ABVD |
| [36271128](https://pubmed.ncbi.nlm.nih.gov/36271128/) | 2022 | 回溯性研究 | Sci Rep | 245 名接受 ABVD 的患者，評估期中 FDG-PET/CT 的預後預測價值 |
| [33258329](https://pubmed.ncbi.nlm.nih.gov/33258329/) | 2020 | 回溯性研究 | J Korean Med Sci | 韓國兒童、青少年與年輕成人何杰金氏淋巴瘤的臨床特徵與治療結果 |
| [32053083](https://pubmed.ncbi.nlm.nih.gov/32053083/) | 2020 | 前臨床 | Anticancer Agents Med Chem | Benzisothiazolone 衍生物抑制 NF-κB，並與 doxorubicin、etoposide 有協同作用（細胞實驗） |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-06215 | DAUNOBLASTINA FOR INJ 20MG | 未載明 | 未載明 |

持有人：PFIZER CORPORATION HONG KONG LIMITED。

## 細胞毒性

以下依蒽環類藥物的一般特性判斷，資料包中沒有 daunorubicin 的毒性資料：

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（蒽環類） |
| 骨髓抑制風險 | 高（蒽環類常見嗜中性白血球、血小板減少） |
| 致吐性分級 | 中 |
| 監測項目 | CBC（含分類）、肝腎功能、心功能（如 LVEF；蒽環類有累積劑量相關心毒性） |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

實際風險分級與監測要求，請以原廠仿單為準。

## 安全性考量

安全性資訊請參考原廠仿單。香港衛生署仿單的警語與禁忌尚未取得，藥物交互作用查詢也沒有結果。

## 結論與下一步

**決策：Hold**

**理由：**
- 模型分數很高，但所有臨床試驗與文獻都沒有直接檢驗 daunorubicin。標準方案使用的是 doxorubicin，daunorubicin 是否有額外價值完全沒有證據。
- 香港許可證未載明適應症，仿單安全性資料也缺失，暫時無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊適應症、警語與禁忌。
- 補充 daunorubicin 的作用機轉資料（DrugBank）。
- 檢索 daunorubicin 用於何杰金氏淋巴瘤的直接臨床資料，並與 doxorubicin 做比較。
- 若要推進，先擬定心毒性與骨髓抑制的監測計畫。

其餘 9 個預測適應症的證據更弱（多為 L4 或 L5），目前建議同樣暫緩或僅視為研究問題。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

