---
layout: default
title: Lovastatin
parent: 中證據等級 (L3-L4)
nav_order: 465
evidence_level: L3
indication_count: 5
---

# Lovastatin
{: .fs-9 }

證據等級: **L3** | 預測適應症: **5** 個
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

# LOVASTATIN：從高膽固醇血症到同型合子家族性高膽固醇血症

## 一句話總結

Lovastatin 是最早上市的 HMG-CoA reductase 抑制劑（statin）之一，原用於高膽固醇血症／混合性血脂異常治療。
TxGNN 模型預測它可能對**同型合子家族性高膽固醇血症 (Homozygous Familial Hypercholesterolemia, HoFH)** 有效，
目前有 **3 個臨床試驗**（均非 lovastatin 特異）和 **19 篇文獻**（其中 7 篇直接涉及 lovastatin 用於此族群），但關鍵研究顯示效果可能有限。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高膽固醇血症／血脂異常（statin 類藥物核心適應症；香港無許可證資料可查證） |
| 預測新適應症 | 同型合子家族性高膽固醇血症 (Homozygous Familial Hypercholesterolemia) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

DrugBank 未提供 lovastatin 的正式 MOA 欄位資料（Data Gap），但依據其藥物類別已知：lovastatin 屬 HMG-CoA reductase 抑制劑，透過抑制肝臟膽固醇合成，代償性上調 LDL 受體（LDLR）表現，藉此降低血中 LDL-C，此為 statin 類藥物的核心機轉，已在高膽固醇血症與異型合子家族性高膽固醇血症中證實有效（本 Evidence Pack 的預測清單中，rank 2「hyperlipoproteinemia」與 rank 4「familial hypercholesterolemia」即反映此一成熟、非新穎的適應症）。

然而 TxGNN 排名最高的預測——**同型合子 FH（HoFH）**——在機轉上存在重大限制：HoFH 患者（尤其 receptor-negative 型）先天缺乏功能性 LDL 受體，statin 賴以降 LDL-C 的「上調受體」機轉在此族群基礎被削弱。文獻證據也印證此疑慮：PMID 3397806（Uauy et al., 1988）直接指出 receptor-negative HoFH 兒童使用 lovastatin 治療後，LDL 濃度與代謝並無改善。因此這個預測反映的較可能是「同一疾病譜系（膽固醇代謝異常）」的關聯性，而非機轉上穩健的新適應症。

## 臨床試驗證據

目前登記的臨床試驗均非測試 lovastatin，而是同一疾病族群中其他藥物（alirocumab、ezetimibe）的背景試驗，僅供參考：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | 已完成 | 18 | 測試 alirocumab（非 lovastatin）於 8-17 歲 HoFH 兒少之 LDL-C 療效 |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | 已完成 | 44 | 測試 ezetimibe 併用 atorvastatin/simvastatin 之長期安全性，非 lovastatin |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | 已完成 | 50 | 測試 ezetimibe 併用其他 statin 之療效安全性，非 lovastatin |

## 文獻證據

以下優先列出直接涉及 lovastatin 用於 HoFH／同型合子族群的文獻：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3397806](https://pubmed.ncbi.nlm.nih.gov/3397806/) | 1988 | Clinical Study | The Journal of Pediatrics | Receptor-negative HoFH 兒童使用 lovastatin 治療，**LDL-C 濃度與代謝並未改善**（負向結果） |
| [1785747](https://pubmed.ncbi.nlm.nih.gov/1785747/) | 1991 | Clinical Study | Anales Españoles de Pediatría | HoFH 病童以 lovastatin 併用 probucol、cholestyramine，總膽固醇下降 41.7% |
| [3534334](https://pubmed.ncbi.nlm.nih.gov/3534334/) | 1986 | Case Report | JAMA | HoFH 病童肝臟移植後恢復部分 LDL 受體活性，再併用 lovastatin 達到正常膽固醇值 |
| [2209665](https://pubmed.ncbi.nlm.nih.gov/2209665/) | 1990 | Case Report | European Journal of Pediatrics | HoFH 病童 LDL 血漿分離術併用 lovastatin，長期耐受良好、黃色瘤消退 |
| [2252289](https://pubmed.ncbi.nlm.nih.gov/2252289/) | 1990 | Case Report | Anales Españoles de Pediatría | Receptor-defective HoFH 病例，cholestyramine 併用 lovastatin 有反應 |
| [8637439](https://pubmed.ncbi.nlm.nih.gov/8637439/) | 1996 | Case Report | Metabolism | 同型合子 sitosterolemia 病例，lovastatin 與 cholestyramine 對血漿固醇的效果相反 |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review | Annals of the NY Academy of Sciences | 兒童血脂異常藥物治療綜述，lovastatin 為其中一項成功降脂選項 |

## 香港上市資訊

LOVASTATIN 目前未於香港取得任何藥品許可證（總許可證數：0），無許可證資料可列。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 唯一直接檢視 lovastatin 於 receptor-negative HoFH 效果的研究（PMID 3397806）顯示**無效**，機轉上因該族群缺乏功能性 LDL 受體而受限，與 TxGNN 高分預測形成矛盾；現有正向案例報告多見於 receptor-defective 型或合併其他療法（血漿分離術、肝移植、cholestyramine），難以歸因於 lovastatin 單獨效果。
- 證據等級僅 L3（觀察性/病例報告層級），無 lovastatin 特異性 RCT。
- 藥物於香港尚未取得許可證（0 張），即使證據充分也無法立即臨床應用。

**若要推進需要：**
- 補齊 DG001（仿單警語/禁忌，Blocking）與 DG002（MOA，High）兩項關鍵資料缺口
- 依 LDL 受體殘餘活性分層（receptor-negative vs receptor-defective），釐清可能有反應的 HoFH 亞群
- 若評估市場導入，需先完成香港藥品許可證申請程序
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

