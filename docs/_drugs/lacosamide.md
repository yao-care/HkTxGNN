---
layout: default
title: Lacosamide
parent: 僅模型預測 (L5)
nav_order: 501
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
monitor_inn: "Lacosamide"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "trichotillomania", "nephrogenic syndrome of inappropriate antidiuresis", "migraine disorder", "insomnia (disease)", "migraine with brainstem aura", "myofascial pain syndrome", "obsessive-compulsive disorder", "papillary conjunctivitis"]
description: "Lacosamide：預測新適應症為Manic bipolar affective disorder（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Lacosamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Lacosamide: Manic bipolar affective disorder
{: .text-alpha }

## 一句話總結

Lacosamide 是一種鈉離子通道調節型抗癲癇藥物，在香港已有上市許可證，但本報告所整理的資料中未列出原核准適應症文字。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，目前有 **4 個臨床試驗**和 **18 篇文獻**支持這個方向，其中包含 1 篇 2026 年發表的隨機對照試驗。

> 說明：TxGNN 預測分數最高者為「躁期雙相情感障礙」，但該適應症無臨床試驗，證據等級僅 L3。本報告以證據最完整的「偏頭痛」作為主要評估對象，其他候選於文末列出供參考。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Manic bipolar affective disorder |
| TxGNN 預測分數 | 0.9996 |
| 證據等級 | L5（有 ≥2 個已完成的 Phase 3 試驗，但療效結果尚待核實） |
| 香港上市 | 上市中（有效許可證 12 張／共 12 張） |
| 許可證數 | 12 張（有效 12 張） |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料庫記錄。根據已知文獻，Lacosamide 能增強電壓門控鈉離子通道的緩慢失活，並可能調節 CRMP2 蛋白，進而降低神經元過度興奮。

偏頭痛與神經元過度興奮、皮質擴散性抑制（cortical spreading depolarization）有關。小鼠研究顯示 Lacosamide 對皮質擴散性抑制有作用；另有研究提出，Lacosamide 經由 CRMP2 可能抑制三叉神經系統釋放降鈣素基因相關胜肽（CGRP）。抗癲癇藥物本來就常用於偏頭痛預防，因此機轉上具合理性。

需注意的是，目前提供的資料並未包含各試驗的療效結果，因此「有效」仍屬假說，需對照已發表結果驗證。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05851781](https://clinicaltrials.gov/study/NCT05851781) | Phase 3 | 完成 | 600 | Lacosamide 對比 propranolol 用於偏頭痛，主要指標為每月頭痛天數減少及 ≥50% 反應率（無結果資料） |
| [NCT06243692](https://clinicaltrials.gov/study/NCT06243692) | Phase 3 | 未知 | 600 | Lacosamide 對比 topiramate 用於偏頭痛（狀態未知，完成與否不確定） |
| [NCT05632133](https://clinicaltrials.gov/study/NCT05632133) | Phase 3 | 完成 | 200 | 隨機試驗，評估 Lacosamide 對偏頭痛患者血清 CGRP 濃度的影響（偏機轉/生物標記，階段標示與先導研究設計不一致） |
| [NCT00440518](https://clinicaltrials.gov/study/NCT00440518) | Phase 2 | 完成 | 218 | 多中心、雙盲、安慰劑對照，評估 100 與 300 mg/日用於預防偏頭痛（試驗標題不完整，適應症需再確認） |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41863672](https://pubmed.ncbi.nlm.nih.gov/41863672/) | 2026 | RCT | Mol Neurobiol | Lacosamide 對比 propranolol 預防發作性偏頭痛的雙盲試驗，探討作為無法耐受 propranolol 者的替代選項 |
| [38502425](https://pubmed.ncbi.nlm.nih.gov/38502425/) | 2024 | RCT | Acta Neurol Belg | 評估 Lacosamide 對發作性偏頭痛患者血清 CGRP 的影響 |
| [22779776](https://pubmed.ncbi.nlm.nih.gov/22779776/) | 2013 | 系統性回顧/統合分析 | Epilepsia | Lacosamide 隨機試驗的不良事件概況（安全性參考） |
| [22862686](https://pubmed.ncbi.nlm.nih.gov/22862686/) | 2012 | Review | Expert Opin Emerg Drugs | 慢性與難治型偏頭痛的新興治療 |
| [40670944](https://pubmed.ncbi.nlm.nih.gov/40670944/) | 2025 | 前臨床 | J Headache Pain | Lacosamide 對小鼠皮質擴散性抑制的影響 |
| [27917413](https://pubmed.ncbi.nlm.nih.gov/27917413/) | 2016 | 前臨床 | Pain Rep | (S)-Lacosamide 在頭面部疼痛模型中，經 CRMP2 抑制 CGRP 釋放 |
| [35696452](https://pubmed.ncbi.nlm.nih.gov/35696452/) | 2022 | Review | Brain | SCN1A 功能獲得型疾病譜，與家族性偏癱型偏頭痛相關 |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Rev Neurother | 三叉神經痛藥物治療更新（間接相關） |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-61177 | VIMPAT TAB 150MG（UCB） | 錠劑 | 本次資料未提供 |
| HK-61175 | VIMPAT TAB 50MG（UCB） | 錠劑 | 本次資料未提供 |
| HK-61176 | VIMPAT TAB 100MG（UCB） | 錠劑 | 本次資料未提供 |
| HK-62585 | VIMPAT SYRUP 10MG/ML（UCB） | 糖漿 | 本次資料未提供 |
| HK-61174 | VIMPAT SOLUTION FOR INFUSION 10MG/ML（UCB） | 輸注溶液 | 本次資料未提供 |

另有 7 張許可證為學名藥或其他品牌（LACOSAMIDE TABLETS、LACOTROL、LACOSAMIDE GENEPHARM），共 12 張，皆為有效單方製劑。

---

## 安全性考量

- **知識圖譜標示的相關疾病（非仿單文字）**：直立性低血壓、姿勢性心搏過速症候群、多系統萎縮、肝臟疾病、膽囊疾病、心房顫動、心房撲動、冠狀動脈疾病、心肌缺血、房室傳導阻滯、病竇症候群等。多數與心臟傳導及自主神經功能相關，須特別留意。
- **藥物交互作用**：共 25 筆，列出的主要項目如下。
  - 重度：Dolasetron、Ceritinib、Siponimod
  - 中度：Clarithromycin、Ethanol、Cobicistat、Chloroquine、Hydroxychloroquine、Mefloquine、Lidocaine、Ketoconazole、Pasireotide、Alectinib、Brigatinib、Crizotinib、Fingolimod、Idelalisib、Imatinib、Ozanimod、Sunitinib 等
- **文獻中的安全訊號**：有 Lacosamide 誘發雙相情感障礙患者嗜中性白血球減少的個案報告。

仿單警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 偏頭痛有 3 個 Phase 3 試驗（2 個已完成、1 個狀態未知）和 1 篇 2026 年 RCT，且前臨床數據提供了機轉支持。
- 但本次資料未包含任何療效結果，且 Phase 3 標示與部分試驗設計不符，因此需先核實結果再推進。

**若要推進需要：**
- 確認 NCT05851781、NCT06243692 及 PMID 41863672 的主要療效終點與安全性結果
- 確認 NCT00440518 實際研究的適應症
- 取得香港原廠仿單（警語、禁忌症、適應症）及 DrugBank 作用機轉資料
- 建立安全監測計畫：心臟傳導（PR 間期）、頭暈、血球計數、藥物交互作用

---

## 其他候選適應症（供參考）

| 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|-----------|-----------|---------|------|
| 躁期雙相情感障礙 | 0.9996 | L5 | Research Question（無臨床試驗；僅有一項回溯性 30 日對照研究及一項 12 週開放標籤先導試驗，另有嗜中性白血球減少個案報告） |
| 肌筋膜疼痛症候群 | 0.9981 | L5 | Research Question（僅有 1 個 Phase 2 纖維肌痛試驗 NCT00401830，無結果，適應症吻合度待確認） |
| 妥瑞氏症 | 0.9995 | L5 | Hold（無支持療效的證據；文獻反而提示抗癲癇藥可能誘發抽動） |
| 腎因性抗利尿激素分泌不當症候群 | 0.9991 | L5 | Hold（無證據，且抗癲癇藥可能引起低血鈉） |
| 伴腦幹先兆偏頭痛 | 0.9982 | L5 | Hold（僅有間接機轉支持） |
| 拔毛症、失眠、強迫症、乳突性結膜炎 | 0.9972–0.9992 | L5 | Hold（無相關證據） |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

