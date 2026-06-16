---
layout: default
title: Fosaprepitant
parent: 僅模型預測 (L5)
nav_order: 334
evidence_level: L5
indication_count: 5
---

# Fosaprepitant
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

# Fosaprepitant：從化療止吐到腎源性抗利尿不當症候群

## 一句話總結

Fosaprepitant 是 Aprepitant 的靜脈注射前驅藥，為 NK1（神經激肽-1）受體拮抗劑，核准用於預防化療引發的噁心嘔吐（CINV）。
TxGNN 模型本次預測了 **5 個潛在新適應症**，排名第一的是**腎源性抗利尿不當症候群（NSIAD）**，預測分數達 99.92%，
然而 5 個預測均無任何直接臨床試驗或文獻支持，機轉合理性存疑，全部建議 **Hold**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 化療引發噁心嘔吐（CINV）預防 |
| 預測新適應症（排名第一） | 腎源性抗利尿不當症候群（Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD） |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L5（5 個預測全部） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold（5 個預測全部） |

---

## 所有預測適應症一覽

| 排名 | 疾病名稱 | TxGNN 分數 | 證據等級 | 建議 |
|------|---------|-----------|---------|------|
| 1 | 腎源性抗利尿不當症候群（NSIAD） | 99.92% | L5 | Hold |
| 2 | 肺囊蟲肺炎（Pneumocystosis） | 99.87% | L5 | Hold |
| 3 | 麻風病（Leprosy） | 99.82% | L5 | Hold |
| 4 | 隱球菌腦膜炎（Cryptococcal Meningitis） | 99.79% | L5 | Hold |
| 5 | 多發性內分泌腫瘤（Multiple Endocrine Neoplasia） | 99.76% | L5 | Hold |

---

## 為什麼這個預測合理？

Fosaprepitant 在體內迅速水解轉換為活性成分 Aprepitant，作用機轉為選擇性阻斷 NK1（神經激肽-1）受體，抑制 Substance P 與受體結合，從而抑制大腦嘔吐中樞的化療相關嘔吐反射。

> **注意**：本 Evidence Pack 標記 MOA 欄位為資料缺漏，以上機轉說明依藥理文獻補充，非原始資料來源。

### 各預測的機轉分析

**① 腎源性抗利尿不當症候群（NSIAD）**
NSIAD 由 AVPR2（V2 加壓素受體）基因功能增益突變所致，導致腎臟持續性過度保水、低血鈉。NK1 受體拮抗與 AVPR2/AVP（arginine vasopressin）訊號通路無已知交互作用；TxGNN 高分可能源自知識圖譜中腎臟節點的間接關聯，**缺乏生物機轉合理性**。

**② 肺囊蟲肺炎（Pneumocystosis）**
PCP 主要侵犯免疫功能低下患者，病原體為 *Pneumocystis jirovecii*（真菌）。NK1/Substance P 軸雖在肺部免疫調節中有一定角色（如支氣管張力、神經性炎症），但無任何研究顯示 NK1 拮抗對真菌病原有清除效果；CINV 用途中的化療背景可能在知識圖譜中造成**假性關聯**。

**③ 麻風病（Leprosy）**
麻風分枝桿菌（*Mycobacterium leprae*）感染以周邊神經侵犯與慢性神經炎症為特徵。Substance P 在周邊神經系統中扮演神經肽角色，理論上 NK1 拮抗可能影響神經炎症反應，然而：(1) 無任何前臨床或臨床研究支持；(2) NK1 通路與抗菌機制無直接連結。**機轉推測等級極低**。

**④ 隱球菌腦膜炎（Cryptococcal Meningitis）**
NK1 受體廣泛分佈於中樞神經系統，Substance P 在神經炎症與血腦屏障（BBB）通透性調節中有作用，理論上 NK1 拮抗可能減輕 CNS 炎症。然而：(1) 針對隱球菌腦膜炎的前臨床或臨床證據為零；(2) Fosaprepitant 無抗真菌活性；若有任何治療潛力，最多是**輔助抗炎**而非主要治療，且仍需前臨床驗證。

**⑤ 多發性內分泌腫瘤（MEN）**
MEN 由 *MEN1*、*RET* 等基因突變導致多腺體腫瘤化，與 NK1 受體通路無已知交集。檢索到的 3 項臨床試驗均為 **CINV 止吐用途**（Aprepitant/Fosaprepitant 作為支持性照護），受試者為接受化療的腫瘤患者，而非 MEN 治療試驗，屬**典型假性關聯（confounded association）**。

---

## 臨床試驗證據

### 排名 1–4（NSIAD、Pneumocystosis、Leprosy、Cryptococcal Meningitis）

目前無相關臨床試驗登記。

### 排名 5：多發性內分泌腫瘤

> ⚠️ 以下 3 項試驗均為止吐（CINV）適應症研究，**與 MEN 治療無直接關聯**（相關性評級：C）。列出僅供機轉假性關聯說明之用。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00293384](https://clinicaltrials.gov/study/NCT00293384) | NA | 完成 | 40 | Aprepitant + granisetron + dexamethasone 預防高劑量 Cyclophosphamide 化療後 CINV，用於自體幹細胞移植前造血幹細胞動員期間 |
| [NCT00248547](https://clinicaltrials.gov/study/NCT00248547) | NA | 完成 | 40 | Aprepitant vs 安慰劑聯合 Ondansetron + Dexamethasone，用於造血細胞移植（HCT）後 CINV 控制的隨機試驗 |
| [NCT01736917](https://clinicaltrials.gov/study/NCT01736917) | Phase 2 | 完成 | 65 | Fosaprepitant（IV）+ 5HT3 拮抗劑 + Dexamethasone 用於生殖細胞腫瘤患者接受 5 天 Cisplatin 化療的 CINV 預防；為首個 Fosaprepitant 多日 Cisplatin 場景臨床試驗 |

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Fosaprepitant 目前在香港**未上市**，無任何許可證記錄。

如需確認，可查詢香港衛生署藥物辦公室（https://www.drugoffice.gov.hk/）或比對 Aprepitant（其口服活性型）的上市狀態。

---

## 安全性考量

安全性資訊請參考原廠仿單。

本 Evidence Pack 安全性欄位（警語、禁忌、DDI）均為資料缺漏，DDI 查詢結果為 0 筆，資安初評（S1）目前無法執行。

---

## 結論與下一步

**決策：Hold（5 個預測適應症全部）**

**理由：**
全部 5 個預測適應症均為 L5 等級，無直接臨床試驗或文獻支持；機轉分析顯示 NK1 受體拮抗與各預測疾病的病生理均無合理連結，其中 MEN 所關聯的 3 項臨床試驗屬假性關聯，不構成治療證據。

**若要推進需要：**
- 補充 MOA 詳細資料（DrugBank API 查詢 DB06717）
- 補充香港/台灣上市安全性資訊（原廠仿單 PDF 解析），解除 DG001 阻塞項
- 針對機轉合理性最高的**隱球菌腦膜炎**候選，搜尋 NK1 拮抗劑在 CNS 炎症的前臨床文獻，評估是否有輔助治療研究空間
- 確認香港是否有 Aprepitant（口服活性型）上市，以補充藥物可及性評估
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

