---
layout: default
title: Donepezil
parent: 僅模型預測 (L5)
nav_order: 292
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
monitor_inn: "Donepezil"
predicted_indications: ["psychogenic movement disorders", "chronic tic disorder", "primary orthostatic tremor", "benign shuddering attacks", "extrapyramidal and movement disease", "tremor-nystagmus-duodenal ulcer syndrome", "benign paroxysmal tonic upgaze of childhood with ataxia", "lingual-facial-buccal dyskinesia"]
description: "Donepezil：預測新適應症為Psychogenic movement disorders（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Donepezil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Donepezil: Psychogenic movement disorders
{: .text-alpha }

## 一句話總結

Donepezil 是乙醯膽鹼酯酶抑制劑，原本用於阿茲海默症等失智相關疾病的治療。
TxGNN 模型預測它可能對**慢性抽動障礙 (Chronic Tic Disorder)** 有效（預測排名第 2），
目前**沒有登記的臨床試驗**，僅有 **5 篇文獻**（以小規模開放標籤研究、個案報告與動物實驗為主）支持這個方向。

> 本報告以排名第 2 的「慢性抽動障礙」作為主要評估對象，原因是排名第 1 的「心因性動作障礙」完全沒有試驗或文獻，無法進行有意義的評估。其他預測適應症於文末簡要整理。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Psychogenic movement disorders |
| TxGNN 預測分數 | 0.9923 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 20 張 |
| 建議決策 | Hold（列為研究問題，尚不建議推進） |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Donepezil 屬於乙醯膽鹼酯酶抑制劑類別，可提升腦內乙醯膽鹼濃度，其在阿茲海默症中的療效已被證實。

抽動症與紋狀體（基底核）的膽鹼功能異常有關，膽鹼系統又會與多巴胺、血清素系統交互作用，進而影響抽動的表現。小鼠實驗（DOI 誘發的頭部抽動反應，被視為抽動模型）顯示 Donepezil 可減弱此反應，支持這個假說。

臨床方面，有兒童與青少年抽動合併注意力不足過動症 (ADHD) 的開放標籤研究，以及少數個案報告顯示可能有益。但這些證據規模小、缺乏對照組，尚不足以確認療效。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [18343255](https://pubmed.ncbi.nlm.nih.gov/18343255/) | 2008 | 臨床研究（18 週開放標籤、單中心、劑量遞增） | Clinical Therapeutics | 探討 Donepezil 用於兒童與青少年抽動合併 ADHD，基於紋狀體膽鹼功能異常的假說 |
| [10440471](https://pubmed.ncbi.nlm.nih.gov/10440471/) | 1999 | 個案報告/小型系列 | J Clin Psychopharmacol | Donepezil 用於妥瑞氏症與 ADHD 的初步報告 |
| [16986157](https://pubmed.ncbi.nlm.nih.gov/16986157/) | 2006 | 評論/個案為基礎 | Movement Disorders | 討論 Donepezil 對妥瑞氏症是否同樣有效 |
| [16045972](https://pubmed.ncbi.nlm.nih.gov/16045972/) | 2005 | 前臨床（小鼠） | Pharmacol Biochem Behav | 比較 Donepezil、尼古丁與 haloperidol 對中樞血清素系統的影響，作為妥瑞氏症模型 |
| [14643839](https://pubmed.ncbi.nlm.nih.gov/14643839/) | 2003 | 前臨床（小鼠） | Pharmacol Biochem Behav | Donepezil 可減弱 DOI 誘發的頭部抽動反應 |

---

## 香港上市資訊

香港共有 20 張有效單一成分許可證，無已註銷者。以下列出 5 張主要許可證（資料中未提供劑型與核准適應症文字）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-42889 | ARICEPT TAB 10MG（衛采 Eisai） | 錠劑 | 資料未載明 |
| HK-61846 | ARICEPT TABLETS 23MG（衛采 Eisai） | 錠劑 | 資料未載明 |
| HK-59867 | ALZEDON TAB 5MG（Sandoz） | 錠劑 | 資料未載明 |
| HK-63773 | DONEPEZIL STADA TABLETS 10MG | 錠劑 | 資料未載明 |
| HK-65710 | DONEPEZIL HCL GENEPHARM ORODISPERSIBLE TABLETS 10MG | 口崩錠 | 資料未載明 |

---

## 安全性考量

- **知識圖譜中記錄的禁忌疾病**（非仿單原文，僅供參考）：癲癇、氣喘（含內因性與過敏性）、膀胱頸阻塞、活動性消化性潰瘍、病態竇症候群（含家族性）、房室傳導阻滯。
- **藥物交互作用**：共查得 100 筆，其中列出的主要項目：
  - **重大 (Major)**：Bupropion
  - **中度 (Moderate)**：抗膽鹼藥物（Atropine、Hyoscyamine、Glycopyrronium、Clidinium、Dicyclomine）、H2 受體阻斷劑（Famotidine、Ranitidine、Cimetidine）、Loperamide、Dexamethasone、Metronidazole、Dolasetron 等
  - **輕微 (Minor)**：Aprepitant、Acetylsalicylic acid、Lorcaserin、Clarithromycin
- **動作障礙風險**：2025 年系統性回顧指出，乙醯膽鹼酯酶抑制劑用於阿茲海默症時，可能與動作障礙相關。對於本身就是動作障礙的抽動症，需特別留意是否惡化。

其餘警語與仿單禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 抽動症的證據僅有小規模開放標籤研究、個案報告與小鼠實驗，沒有登記的臨床試驗，也沒有 RCT，屬於「研究問題」階段。
- 香港仿單的警語與禁忌資料尚未取得，無法完成安全性初篩；且已有文獻提示膽鹼酯酶抑制劑可能誘發動作障礙。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症，完成安全性初篩
- 補齊詳細的作用機轉（MOA）資料
- 取得 18343255 研究的完整結果（療效與耐受性）
- 設計小型隨機對照試驗，並納入抽動惡化與膽鹼性副作用的監測
- 評估與常用抽動症藥物（如抗精神病藥）併用時的交互作用

---

## 附錄：其他預測適應症簡要整理

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 說明 |
|------|-----------|-----------|---------|------|
| 1 | 心因性動作障礙 | 0.9923 | L5 | 僅有模型預測，無試驗與文獻 |
| 3 | 原發性姿勢性顫抖 | 0.9917 | L5 | 僅有模型預測 |
| 4 | 良性顫抖發作 | 0.9916 | L5 | 僅有模型預測；屬良性自限性疾病，長期用藥風險效益不佳 |
| 5 | 錐體外徑與動作疾病 | 0.9916 | L5 | 有遲發性動作障礙的小型研究，但也有動作障礙的安全性訊號 |
| 6 | 顫抖-眼震-十二指腸潰瘍症候群 | 0.9915 | L5 | 檢索到的文獻不相關；膽鹼酯酶抑制劑可能增加胃酸分泌而加重潰瘍 |
| 7 | 兒童良性陣發性向上凝視合併共濟失調 | 0.9912 | L5 | 僅有模型預測 |
| 8 | 舌-顏面-頰部運動障礙 | 0.9902 | L5 | 有 Cochrane 回顧討論膽鹼類藥物治療遲發性運動障礙，但並非專門針對 Donepezil，確定性有限 |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

