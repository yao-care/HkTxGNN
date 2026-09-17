---
layout: default
title: Polymyxin B
parent: 僅模型預測 (L5)
nav_order: 597
evidence_level: L5
indication_count: 3
---

# Polymyxin B
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Polymyxin B：從抗菌治療到三個候選新適應症評估

## 一句話總結

Polymyxin B（多黏菌素 B）是作用於革蘭氏陰性菌外膜的抗生素，因目前未於香港上市，原始核准適應症與作用機轉資料暫缺。TxGNN 模型針對此藥預測三個潛在新適應症——**結膜炎**、**支氣管炎**、**喉氣管炎**，三者證據強度差異懸殊：結膜炎已有 **3 個臨床試驗**（含 Phase 3/4 RCT）與 **20 篇文獻**支持，證據等級達 L1；支氣管炎僅有 14 篇文獻、無臨床試驗（L4）；喉氣管炎則完全沒有實證，僅有模型預測分數（L5）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（藥物未於香港上市，無許可證可查） |
| 作用機轉 | 資料缺失 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |

### 三個預測新適應症比較

| 順位 | 預測適應症 | TxGNN 分數 | TxGNN KG 排名 | 臨床試驗數 | 文獻數 | 證據等級 | 建議決策 |
|------|-----------|-----------|--------------|-----------|--------|---------|---------|
| 1 | 支氣管炎 (Bronchitis) | 99.87% | #3366 | 0 | 14 | L4 | Hold |
| 2 | 喉氣管炎 (Laryngotracheitis) | 99.62% | #7469 | 0 | 0 | L5 | Hold |
| 3 | 結膜炎 (Conjunctivitis) | 99.06% | #14708 | 3 | 20 | **L1** | **Proceed with Guardrails** |

> 注意：TxGNN 分數與 KG 排名反映模型內部信心，不等於實證強度——分數最高的支氣管炎，實際佐證反而比排名第三的結膜炎弱。

---

## 為什麼這個預測合理？

目前缺乏 Polymyxin B 完整的作用機轉（MOA）資料。根據已知的藥理分類，Polymyxin B 是多黏菌素類抗生素，透過破壞革蘭氏陰性菌外膜磷脂達到殺菌效果，臨床上已廣泛用於治療多重抗藥性革蘭氏陰性菌感染。以下依證據強度說明三個候選適應症的合理性：

**結膜炎（證據最強）**：Polymyxin B 對結膜炎常見致病菌（綠膿桿菌、流感嗜血桿菌）具直接殺菌活性，與 trimethoprim 併方（Polytrim）已是眼科臨床常規用藥多年，機轉對應明確，非推測性關聯。

**支氣管炎（機轉合理但安全訊號矛盾）**：Polymyxin B 對革蘭氏陰性菌（尤其綠膿桿菌）有效，理論上可用於治療細菌性氣管支氣管炎；但文獻同時大量記載吸入 Polymyxin B 會誘發非特異性支氣管收縮（常被用作激發測試藥劑），甚至有「danger of inhalation」的案例報告，顯示療效證據與安全性訊號互相矛盾。

**喉氣管炎（生物學合理性低）**：僅有 TxGNN 知識圖譜預測分數支持，無任何臨床試驗或文獻佐證。喉氣管炎（尤其兒童常見的 croup）多為病毒性病因，與 Polymyxin B 的抗革蘭氏陰性菌機轉缺乏直接對應。

---

## 臨床試驗證據

### 結膜炎

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00581542](https://clinicaltrials.gov/study/NCT00581542) | Phase 4 | 完成 | 124 | 比較 Polytrim（polymyxin B/trimethoprim）與 moxifloxacin 治療兒童結膜炎，已完成，療效終點明確對應本適應症 |
| [NCT01227863](https://clinicaltrials.gov/study/NCT01227863) | Phase 3 | 狀態未知 | 70 | 比較兩款含 polymyxin B 複方（dexamethasone+neomycin+polymyxin B）眼藥水治療急性細菌性結膜炎之療效 |
| [NCT01809483](https://clinicaltrials.gov/study/NCT01809483) | Phase 3 | 完成 | 32 | 主要比較繃帶式隱形眼鏡 vs 加壓包紮治療角膜糜爛，polymyxin B 僅為背景用藥，與結膜炎關聯性弱 |

### 支氣管炎、喉氣管炎

目前無相關臨床試驗登記。

---

## 文獻證據

### 結膜炎

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [19043943](https://pubmed.ncbi.nlm.nih.gov/19043943/) | 2008 | RCT | J Pediatr Ophthalmol Strabismus | Moxifloxacin 與 polymyxin B/trimethoprim 治療兒童細菌性結膜炎比較 |
| [23092529](https://pubmed.ncbi.nlm.nih.gov/23092529/) | 2013 | RCT | J Pediatr | 單盲 RCT，比較 polymyxin B-trimethoprim 與 moxifloxacin 治療兒童急性結膜炎 |
| [19043945](https://pubmed.ncbi.nlm.nih.gov/19043945/) | 2008 | RCT | J Pediatr Ophthalmol Strabismus | 多中心比較 polymyxin B/trimethoprim 與 moxifloxacin 治療細菌性結膜炎起效速度 |
| [6188739](https://pubmed.ncbi.nlm.nih.gov/6188739/) | 1983 | RCT | J Antimicrob Chemother | 多中心試驗，trimethoprim-polymyxin B 對比 neomycin-polymyxin B-gramicidin 及 chloramphenicol 治療細菌性結膜炎 |
| [2850891](https://pubmed.ncbi.nlm.nih.gov/2850891/) | 1988 | RCT | Curr Med Res Opin | 雙盲試驗，trimethoprim-polymyxin B 藥膏對比 chloramphenicol 治療細菌性結膜炎 |
| [2540136](https://pubmed.ncbi.nlm.nih.gov/2540136/) | 1989 | RCT | J Antimicrob Chemother | 四項 RCT 統合分析（528 名患者），trimethoprim-polymyxin B 對比 chloramphenicol |
| [8595639](https://pubmed.ncbi.nlm.nih.gov/8595639/) | 1995 | Cohort | Clin Ther | 兒童急性細菌性結膜炎使用 trimethoprim-polymyxin B 眼藥水之調查結果 |
| [2370842](https://pubmed.ncbi.nlm.nih.gov/2370842/) | 1990 | Review | Med Lett Drugs Ther | Trimethoprim-polymyxin B 用於細菌性結膜炎綜述 |

### 支氣管炎

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23124906](https://pubmed.ncbi.nlm.nih.gov/23124906/) | 2013 | Cohort | Infection | 比較 polymyxin B 與其他抗生素治療 Pseudomonas/Acinetobacter 引起的呼吸器相關肺炎與氣管支氣管炎 |
| [17350201](https://pubmed.ncbi.nlm.nih.gov/17350201/) | 2007 | Cohort | Diagn Microbiol Infect Dis | 吸入型 polymyxin B 用於多重抗藥性革蘭氏陰性菌肺炎與氣管支氣管炎之搶救治療 |
| [231152](https://pubmed.ncbi.nlm.nih.gov/231152/) | 1979 | Cohort | Lung | 氣喘及慢性阻塞性支氣管炎患者對吸入 polymyxin B 的支氣管反應性研究（顯示刺激性風險） |
| [4319158](https://pubmed.ncbi.nlm.nih.gov/4319158/) | 1970 | Case Series | Chest | 支氣管內給予 polymyxin B 治療慢性支氣管炎之實驗觀察 |
| [4322737](https://pubmed.ncbi.nlm.nih.gov/4322737/) | 1971 | Case Report | Ann Intern Med | 吸入 polymyxin B 之危害案例報告 |

### 喉氣管炎

目前無相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：分適應症判斷**
- 結膜炎：**Proceed with Guardrails**
- 支氣管炎：**Hold**
- 喉氣管炎：**Hold**

**理由：**
結膜炎已有多個 Phase 3/4 RCT 與 6 篇高品質文獻 RCT 支持，且 polymyxin B/trimethoprim 複方已是眼科臨床常規用藥，證據充分可推進。支氣管炎雖有文獻描述抗菌潛力，但同時存在吸入誘發支氣管收縮的安全訊號，證據矛盾，應暫緩。喉氣管炎僅有模型預測分數、無任何實證，生物學合理性低，不建議推進。

**若要推進需要：**
- 補齊 TFDA/藥監局仿單警語與禁忌症資料（目前為 Blocking 等級缺口，無法完成 S1 安全性初評）
- 取得完整作用機轉（MOA）資料以強化機轉關聯性分析
- 若推進結膜炎方向：確認香港上市/許可證申請路徑（目前市場狀態為未上市）
- 若考慮支氣管炎方向：需先釐清吸入劑型的呼吸道刺激性風險與療效證據的矛盾
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

