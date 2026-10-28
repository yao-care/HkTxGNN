---
layout: default
title: Isoflurane
parent: 僅模型預測 (L5)
nav_order: 486
evidence_level: L5
indication_count: 7
monitor_inn: "ISOFLURANE"
predicted_indications: ["Prinzmetal angina", "Tourette syndrome", "manic bipolar affective disorder", "trichotillomania", "dysthymic disorder", "nephrogenic syndrome of inappropriate antidiuresis", "migraine disorder"]
last_modified_at: 2026-10-23
description: "Isoflurane：預測新適應症為Prinzmetal angina（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Isoflurane
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

## Isoflurane: Prinzmetal angina
{: .text-alpha }

## 一句話總結

Isoflurane 是吸入性全身麻醉劑，香港已有 4 張有效許可證，但本報告所整理的資料中，許可證並未載明核准適應症文字。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，目前**無臨床試驗**，僅有 **12 篇文獻**，其中多為與偏頭痛生物學相關的前臨床研究，與 isoflurane 直接相關的只有少數幾篇。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Prinzmetal angina |
| TxGNN 預測分數 | 0.9967 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 4 張／共 4 張） |
| 許可證數 | 4 張（有效 4 張） |
| 建議決策 | Hold（列為研究問題） |

> 說明：另有其他 6 個預測適應症（Prinzmetal 心絞痛、杜瑞氏症、躁期雙極性情感疾患、拔毛症、輕鬱症、腎因性抗利尿激素分泌不當症候群），本報告聚焦於證據最多的偏頭痛。其中除躁期雙極性情感疾患僅有間接文獻外，其餘皆僅有模型預測，無任何臨床試驗或文獻，證據等級為 L5。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，isoflurane 屬於吸入性揮發性麻醉劑，文獻指出其作用涉及 GABA-A 受體與 NMDA 受體，機轉上可能與偏頭痛的神經生理有關。

偏頭痛先兆被認為與皮質擴散性抑制 (cortical spreading depression, SD) 有關。1996 年的一項研究 (PMID 8665587) 發現吸入性麻醉劑可抑制擴散性抑制。另有研究顯示 NMDA 受體拮抗劑會影響擴散性抑制的易感性 (PMID 17267580)，與 isoflurane 的 NMDA 阻斷活性方向一致。此外，一則病例報告 (PMID 26363696) 描述以全身麻醉治療偏濁性偏頭痛持續狀態。

需要注意的是，這些證據均為前臨床或單一病例，且 isoflurane 在部分病人身上可能引起術後頭痛，因此效益與風險的平衡並不明確。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

下表僅列出與 isoflurane／麻醉劑較直接相關的文獻。其餘文獻（PMID 20974582、40764901、27122032、24004534、41836510、24256609、39354357、22523186）屬 CGRP、三叉神經、擴散性去極化等偏頭痛基礎研究，並非針對 isoflurane，僅提供背景脈絡。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26363696](https://pubmed.ncbi.nlm.nih.gov/26363696/) | 2015 | 病例報告 | Rev Bras Anestesiol | 以全身麻醉治療偏頭痛持續狀態；提出 propofol 與 isoflurane 作用於 GABA-A 受體，理論上具研究價值 |
| [26323741](https://pubmed.ncbi.nlm.nih.gov/26323741/) | 2015 | 病例報告 | Braz J Anesthesiol | 同上（英文版本） |
| [8665587](https://pubmed.ncbi.nlm.nih.gov/8665587/) | 1996 | 前臨床 | Cephalalgia | 吸入性麻醉劑可抑制皮質擴散性抑制，與偏頭痛相關 |
| [17267580](https://pubmed.ncbi.nlm.nih.gov/17267580/) | 2007 | 前臨床 | J Pharmacol Exp Ther | NMDA 受體拮抗劑影響大鼠擴散性抑制，顯示偏頭痛治療潛力（非 isoflurane 專屬研究） |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-58404 | TERRELL ISOFLURANE LIQUID FOR INHALATION | 吸入液 | 許可證資料未載明 |
| HK-50284 | ATTANE (ISOFLURANE) LIQ FOR INHAL'N (VET) | 吸入液（獸用） | 許可證資料未載明 |
| HK-51392 | I.S.O. INHALATION ANAESTHETIC LIQUID 1ML/ML (VET) | 吸入液（獸用） | 許可證資料未載明 |
| HK-40926 | ISOFLURANE | 吸入液 | 許可證資料未載明 |

4 張許可證均為單方、有效狀態；其中 2 張品名標示為獸用 (VET)，使用前應確認是否適用於人類。

## 安全性考量

- **知識圖譜中記錄的禁忌關聯**（來自知識圖譜，並非仿單內容）：肝臟疾病、膽囊疾病、低血壓疾患、麻醉引起的惡性高熱、運動誘發性惡性高熱、杜顯氏肌肉失養症、肌肉失養症、貝克氏肌肉失養症。
- **藥物交互作用**：共查得 38 筆。其中**嚴重 (Major)** 為 epinephrine；**中度 (Moderate)** 為 morphine、opium。其餘如 atropine、hydrocortisone、mannitol、pantoprazole、omeprazole、vancomycin 等，嚴重度未分級。

其他警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 偏頭痛是本藥所有預測中證據最多的一項，但全為前臨床研究與單一病例報告，沒有任何臨床試驗直接驗證 isoflurane 對偏頭痛的療效。
- Isoflurane 為吸入性全身麻醉劑，給藥途徑與偏頭痛的慢性預防或急性治療情境落差大，且可能引起術後頭痛，風險效益不明。

**若要推進需要：**
- 補齊作用機轉資料，並釐清 isoflurane 對擴散性抑制的作用強度與劑量
- 取得香港仿單的警語與禁忌資料
- 設計小規模探索性研究（例如僅限難治性偏頭痛持續狀態、住院監測條件下），先評估可行性與安全性
- 評估給藥途徑與麻醉監護需求是否具臨床可行性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

