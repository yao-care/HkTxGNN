---
layout: default
title: Lamotrigine
parent: 僅模型預測 (L5)
nav_order: 497
evidence_level: L5
indication_count: 5
---

# Lamotrigine
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

# Lamotrigine：從癲癇到三叉神經腫瘤（另有更可信的候選：三叉神經痛）

## 一句話總結

Lamotrigine 是已上市的抗癲癇藥，在香港有 20 張許可證。
TxGNN 排名第一的預測是**三叉神經腫瘤 (Trigeminal Nerve Neoplasm)**，但目前**沒有任何臨床試驗**，文獻也只談三叉神經痛，沒有談腫瘤，較可能是疾病名稱對應錯誤。
同一份預測中，**三叉神經痛 (Trigeminal Neuralgia)** 有 4 個臨床試驗和 19 篇文獻，是更值得追蹤的方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 三叉神經腫瘤 (Trigeminal Nerve Neoplasm) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

許可證資料中沒有記載核准適應症，因此本表省略「原適應症」欄。

---

## 為什麼這個預測合理？

Lamotrigine 會阻斷電位門控鈉離子通道，並減少麩胺酸釋放。這個機轉對神經痛和癲癇合理，但對神經腫瘤沒有明確的腫瘤學依據。原始資料中的作用機轉欄位是空的，以上機轉描述來自分析內容。

**這個高分很可能是對應錯誤。** 分數 99.97% 較像是知識圖譜把「三叉神經腫瘤」與「三叉神經痛」混為一談。目前取得的兩篇文獻都在談三叉神經痛，沒有一篇是 lamotrigine 用於腫瘤的研究。

建議先確認疾病名稱的對應是否正確，再投入其他工作。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | 三叉神經痛的內科與外科治療總覽，與腫瘤無關 |
| [30650431](https://pubmed.ncbi.nlm.nih.gov/30650431/) | 2018 | Case report | Stereotact Funct Neurosurg | 海綿狀血管畸形引起三叉神經痛的伽瑪刀放射手術病例，與 lamotrigine 無關 |

---

## 其他預測適應症：三叉神經痛（排名第 2）

TxGNN 分數 99.89%，證據等級 **L2**，建議 **Proceed with Guardrails**。

Lamotrigine 和一線藥 carbamazepine、oxcarbazepine 屬同一類機轉（鈉離子通道阻斷）。目前直接證據僅來自小型試驗，且未提供試驗結果數據。

### 臨床試驗

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00913107](https://clinicaltrials.gov/study/NCT00913107) | Phase 2/3 | 完成 | 21 | Lamotrigine 與 carbamazepine 用於三叉神經痛的療效與安全性比較；最直接的證據，但樣本數小 |
| [NCT00203229](https://clinicaltrials.gov/study/NCT00203229) | 未標示 | 完成 | 20 | 雙盲、安慰劑對照的附加治療試驗；設計嚴謹但樣本數小 |
| [NCT00243152](https://clinicaltrials.gov/study/NCT00243152) | 未標示 | 完成 | 6 | 以 fMRI 評估 lamotrigine 對神經性顏面痛的作用；屬機轉探索，不能證明療效 |
| [NCT04996199](https://clinicaltrials.gov/study/NCT04996199) | Phase 4 | 未知 | 132 | Carbamazepine 與 oxcarbazepine 的比較，未含 lamotrigine，僅作一線用藥背景參考 |

### 文獻（精選 10 篇，共 19 篇）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Guideline | Eur J Neurol | 歐洲神經學會三叉神經痛治療指引；lamotrigine 的定位需查閱指引全文確認 |
| [37892981](https://pubmed.ncbi.nlm.nih.gov/37892981/) | 2023 | 系統性回顧 | Biomedicines | 彙整三叉神經痛藥物治療的療效與副作用 |
| [21621166](https://pubmed.ncbi.nlm.nih.gov/21621166/) | 2011 | 臨床研究 | J Chin Med Assoc | 比較 lamotrigine 與 carbamazepine 的療效與副作用 |
| [30081317](https://pubmed.ncbi.nlm.nih.gov/30081317/) | 2018 | Case report | Mult Scler Relat Disord | 多發性硬化患者的難治性三叉神經痛，以 pregabalin 加 lamotrigine 合併治療成功 |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Rev Neurother | 藥物治療更新；第三代抗癲癇藥可能是輔助或單獨治療的選項 |
| [34108244](https://pubmed.ncbi.nlm.nih.gov/34108244/) | 2021 | Review | Pract Neurol | 三叉神經痛實務指南 |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Review | Mol Pain | 從病理生理到藥物治療的總覽 |
| [30178160](https://pubmed.ncbi.nlm.nih.gov/30178160/) | 2018 | Review | Drugs | 典型與非典型三叉神經痛的現有與創新藥物選項 |
| [39365662](https://pubmed.ncbi.nlm.nih.gov/39365662/) | 2025 | Cohort | Pain | 丹麥全國資料，分析三叉神經痛的共病軌跡 |
| [25299564](https://pubmed.ncbi.nlm.nih.gov/25299564/) | 2014 | Review | BMJ Clin Evid | 三叉神經痛的臨床證據回顧 |

---

## 香港上市資訊

以下列出 5 張主要許可證，資料中未提供劑型與核准適應症。

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-56609 | LAMOTRIGINE-TEVA 100MG TAB | TEVA Pharmaceutical Hong Kong Limited |
| HK-58050 | PMS-LAMOTRIGINE TAB 25MG | Trenton-Boma Ltd |
| HK-66706 | LAMOGA-100 TABLETS 100MG | Health Alliance International Co Ltd |
| HK-68228 | EPSYLAM DT 50 DISPERSIBLE TABLETS 50MG | Hang Lung Trading (H.K.) Co |
| HK-66707 | LAMOGA-25 TABLETS 25MG | Health Alliance International Co Ltd |

---

## 安全性考量

安全性資訊請參考原廠仿單。

三叉神經痛的用藥防護提醒（來自分析內容，非仿單資料）：
- 需緩慢調整劑量，因為有嚴重皮疹和史蒂芬強生症候群的風險。
- 需檢視與 valproate 及酵素誘導劑的藥物交互作用。

---

## 結論與下一步

**決策：Hold（三叉神經腫瘤）；三叉神經痛可 Proceed with Guardrails**

**理由：**
- 三叉神經腫瘤只有模型分數，沒有試驗，文獻也不相關，很可能是疾病對應錯誤。
- 三叉神經痛有 2 個小型的完成試驗（n=21 與 n=20），機轉與一線藥相近，但缺乏大型確認性 Phase 3 試驗，因此為 L2。

**若要推進需要：**
- 檢查 TxGNN 疾病名稱對應，確認「三叉神經腫瘤」是否誤對應到三叉神經痛。
- 取得香港衛生署仿單，補齊警語、禁忌與交互作用資料。
- 查閱歐洲神經學會 2019 指引全文，確認 lamotrigine 是附加或二線用藥。
- 取得 NCT00913107、NCT00203229 的結果數據，確認小型試驗的療效。
- 將 lamotrigine 定位為鈉離子通道一線藥物之後的附加或二線治療。

---

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後方可應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

