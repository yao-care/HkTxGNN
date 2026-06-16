---
layout: default
title: Codeine
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 4
---

# Codeine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Codeine：從鎮痛/止咳到鼻腔疾病（預測）

## 一句話總結

Codeine 是一種阿片類衍生物，廣泛用於鎮痛及止咳，但目前在香港並無任何上市許可。
TxGNN 模型預測其在**鼻腔疾病 (Nasal Cavity Disease)**、**急性咽喉炎**、**三叉神經自律性頭痛**、**過敏性蕁麻疹** 四個方向有潛力。
然而深入分析後發現，現有文獻多描述 Codeine **導致**這些疾病的不良反應而非治療，目前無任何相關臨床試驗，**4 項預測均建議 Hold**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 鎮痛、止咳（全球已知用途；香港無上市紀錄） |
| 預測新適應症（前 4 名） | 鼻腔疾病 / 急性咽喉炎 / 三叉神經自律性頭痛 / 過敏性蕁麻疹 |
| TxGNN 最高預測分數 | 99.93%（鼻腔疾病，Rank 1,994） |
| 證據等級 | L5（所有預測均為模型預測，無治療性研究支持） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | **Hold**（全部 4 項預測） |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（Data Gap）。根據已知資訊，Codeine 是一種天然阿片類生物鹼，在體內代謝後部分轉化為嗎啡（morphine），主要透過活化 **μ-阿片受體（μ-opioid receptor）** 發揮止痛及抑制延髓咳嗽中樞的作用。

各預測適應症的機轉評估如下：

**鼻腔疾病**：Codeine 無已知治療鼻腔疾病之藥理機轉。μ-受體激活理論上可抑制黏膜分泌，但現有兩篇文獻均描述的是鼻腔吸入濫用（intranasal opioid abuse）後造成的**鼻腔壞死或鼻石**，屬藥物濫用之不良結局，與老藥新用概念相悖。

**急性咽喉炎**：Codeine 的止咳作用理論上可緩解相關咳嗽症狀，屬**症狀緩解**而非病因治療。急性咽喉炎通常由病毒或細菌感染引起，Codeine 無抗病毒或抗炎機轉，且目前完全無文獻或臨床試驗支持此用途。

**三叉神經自律性頭痛（TAC）**：雖為阿片類止痛藥，但 TAC（包括叢集性頭痛）的病理機轉涉及三叉神經血管系統及下視丘，與一般傷害性疼痛截然不同。臨床指引明確指出 TAC 患者**不應使用阿片類藥物**，原因是無效且會導致藥物過度使用頭痛（MOH），形成惡性循環。

**過敏性蕁麻疹**：Codeine 透過非免疫機轉**直接刺激肥大細胞脫顆粒（mast cell degranulation）**，釋放組織胺，誘發蕁麻疹。在皮膚科學中，Codeine 廣泛被用作皮內試驗的「**陽性對照**（pseudo-allergic reaction model）」。Codeine 是造成過敏性蕁麻疹的**病因**，而非治療藥物。

---

## 臨床試驗證據

四項預測適應症均無相關臨床試驗登記。

---

## 文獻證據

### 鼻腔疾病（2 篇文獻）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [22965281](https://pubmed.ncbi.nlm.nih.gov/22965281/) | 2012 | Case Report | The Laryngoscope | 鼻腔吸入 hydrocodone-acetaminophen 濫用導致鼻腔及咽部壞死；屬不良反應報告，**非治療用途** |
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Case Report | Ear, Nose & Throat J | Codeine 與鴉片混合物在鼻腔形成鼻石（opioma）；屬異物殘留不良結局，**非治療用途** |

### 三叉神經自律性頭痛（4 篇相關文獻）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [18563291](https://pubmed.ncbi.nlm.nih.gov/18563291/) | 2008 | Case Report | J Headache and Pain | Brugada ECG 患者因無法使用鈉離子通道阻斷劑，例外使用 codeine phosphate 有效；屬特殊個案，非常規治療 |
| [19109043](https://pubmed.ncbi.nlm.nih.gov/19109043/) | 2009 | Retrospective Series | Eur J Paediatric Neurology | 兒童叢集性頭痛臨床特徵描述；非 Codeine 治療研究 |
| [41428068](https://pubmed.ncbi.nlm.nih.gov/41428068/) | 2026 | Case Report | Annales de biologie clinique | 叢集性頭痛患者濫用古柯鹼等物質；警示阿片類物質濫用風險 |
| [26524707](https://pubmed.ncbi.nlm.nih.gov/26524707/) | 2016 | Case Report | American J Medicine | 叢集性頭痛伴昏厥個案報告；非 Codeine 治療研究 |

### 過敏性蕁麻疹（10 篇相關文獻）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [8792922](https://pubmed.ncbi.nlm.nih.gov/8792922/) | 1996 | RCT | Allergy | Mizolastine 治療蕁麻疹 RCT；Codeine 作為**皮試陽性對照**使用，非治療藥物 |
| [16461991](https://pubmed.ncbi.nlm.nih.gov/16461991/) | 2006 | Review | Clinical Reviews in Allergy & Immunology | 綜述指出 Codeine 等阿片類直接激活肥大細胞引起蕁麻疹，屬**藥物不良反應** |
| [3711548](https://pubmed.ncbi.nlm.nih.gov/3711548/) | 1986 | Clinical Study | J Allergy and Clinical Immunology | 皮內注射 codeine 作為肥大細胞脫顆粒陽性對照；蕁麻疹患者皮試反應更敏感 |
| [17210040](https://pubmed.ncbi.nlm.nih.gov/17210040/) | 2007 | Experimental | Clinical and Experimental Allergy | 研究皮膚試驗模型中組織胺與 codeine 的反應模式；Codeine 為試驗工具 |
| [2306020](https://pubmed.ncbi.nlm.nih.gov/2306020/) | 1990 | Clinical Study | Annals of Allergy | 甲狀腺亢進患者對 codeine 皮試反應增強；Codeine 為肥大細胞釋放實驗工具 |
| [2244707](https://pubmed.ncbi.nlm.nih.gov/2244707/) | 1990 | Clinical Study | Annals of Allergy | 慢性蕁麻疹患者對 codeine 皮試更敏感，與肥大細胞密度增加相關 |
| [2941218](https://pubmed.ncbi.nlm.nih.gov/2941218/) | 1986 | Case Report | Contact Dermatitis | 口服 codeine 引起遲發型過敏性蕁麻疹；屬**不良反應**報告 |
| [31066088](https://pubmed.ncbi.nlm.nih.gov/31066088/) | 2019 | Case Series | Contact Dermatitis | 阿片類藥物製造廠工人發生職業性接觸性皮膚炎；屬職業暴露不良反應 |
| [6838021](https://pubmed.ncbi.nlm.nih.gov/6838021/) | 1983 | Clinical Study | Annals of Allergy | 皮內注射 codeine 引起的早期風疹塊反應不易進展至晚期皮膚過敏反應 |
| [6156489](https://pubmed.ncbi.nlm.nih.gov/6156489/) | 1980 | Clinical Study | Schweiz Med Wochenschr | Codeine 磷酸鹽皮試可評估肥大細胞反應性；Codeine 為皮試研究工具 |

---

## 香港上市資訊

Codeine 目前在香港**無任何上市許可**（0 張許可證），無相關上市資訊可列。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold（全部 4 項預測）**

**理由：**

| 預測適應症 | Hold 原因 |
|-----------|----------|
| 鼻腔疾病 | 文獻描述的是 Codeine 濫用造成的鼻腔損傷，與治療目的完全相悖 |
| 急性咽喉炎 | 無任何文獻或臨床試驗支持；僅有理論止咳效益，不治療病因 |
| 三叉神經自律性頭痛 | 臨床指引明確禁用阿片類藥物，使用反會導致 MOH 惡性循環 |
| 過敏性蕁麻疹 | Codeine 本身即為肥大細胞激活劑（病因），非治療藥物 |

**⚠️ 模型評估建議：**

本案例高度疑似 TxGNN 知識圖譜中的**False Positive**。模型可能因以下原因產生誤判：
- Codeine 在文獻中頻繁與這些疾病共同出現（但為**不良反應/試驗工具**關係，非治療關係）
- 知識圖譜可能未能區分「致病關聯」與「治療關聯」

**若要重新評估需要：**
- 補充 Codeine 完整 MOA 及 DrugBank categories 資料
- 查詢香港衛生署管制藥物許可證資料庫
- 在 TxGNN 模型中標注此案例為 False Positive，用於模型校正
- 審視知識圖譜中 Codeine 的連結類型標注，區分「adverse」與「therapeutic」邊緣
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

