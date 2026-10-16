---
layout: default
title: Bupropion
parent: 僅模型預測 (L5)
nav_order: 139
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Bupropion：預測新適應症為注意力不足過動症 (Attention Deficit-Hyperactivity Disorder)（證據等級 L5）。原適應症：憂鬱症、焦慮症、尼古丁依賴等"
monitor_inn: "Bupropion"
predicted_indications: ["attention deficit-hyperactivity disorder", "attention deficit hyperactivity disorder, inattentive type", "faciodigitogenital syndrome", "specific developmental disorder", "chondromyxoid fibroma", "proximal 16p11.2 microdeletion syndrome", "hypervitaminosis", "benign paroxysmal torticollis of infancy", "trigeminal nerve neoplasm", "obsolete hypertelorism (disease)"]
---

# Bupropion
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

# Bupropion：從憂鬱症與戒菸到注意力不足過動症 (ADHD)

## 一句話總結

Bupropion 原本用於重度憂鬱症、焦慮相關疾患及尼古丁依賴（戒菸）的治療。
TxGNN 模型預測它可能對**注意力不足過動症 (Attention Deficit-Hyperactivity Disorder)** 有效，
目前有 **6 個臨床試驗**（其中 1 個為已完成的 Phase 3 隨機對照試驗）和 **20 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 憂鬱症、焦慮症、尼古丁依賴等（依知識圖譜適應症資料；香港許可證未載明核准適應症文字） |
| 預測新適應症 | 注意力不足過動症 (Attention Deficit-Hyperactivity Disorder) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L2（僅 1 個已完成的 Phase 3 RCT，另有系統性回顧與統合分析） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Proceed with Guardrails |

> 註：資料彙整中的自動評等為 L1，但依判定規則（≥2 個已完成的 Phase 3 RCT 才屬 L1），目前僅有 1 個已完成的 Phase 3 RCT（NCT00048360），故本報告判定為 L2。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料庫條目。依文獻所述，Bupropion 的主要作用是抑制去甲腎上腺素與多巴胺的再回收，且不具血清素活性。

ADHD 的病理生理與腦內去甲腎上腺素和多巴胺功能失調有關。現有 ADHD 藥物（如興奮劑、atomoxetine）也作用於這些兒茶酚胺路徑。因此 Bupropion 在機轉上有合理依據，可能改善注意力並減少過動。同時，憂鬱症與 ADHD 常共病，Bupropion 在憂鬱症的療效也支持其在這類族群的應用。

TxGNN 給出極高分數，與上述藥理推論一致。但臨床上 Bupropion 多被視為非興奮劑的替代選項，通常用於對興奮劑無反應或無法耐受的成人患者。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00048360](https://clinicaltrials.gov/study/NCT00048360) | Phase 3 | 完成 | 162 | 成人 ADHD 的 8 週、雙盲、安慰劑對照、彈性劑量（延長釋放劑型 300–450 mg/日）試驗，評估療效與安全性 |
| [NCT00936299](https://clinicaltrials.gov/study/NCT00936299) | Phase 4 | 完成 | 105 | Bupropion 用於合併物質使用障礙的青少年 ADHD |
| [NCT00061087](https://clinicaltrials.gov/study/NCT00061087) | Phase 2/3 | 完成 | 115 | 美沙酮治療患者中的成人 ADHD 治療 |
| [NCT01270555](https://clinicaltrials.gov/study/NCT01270555) | 不適用 | 完成 | 32 | Bupropion SR 用於近期或目前有物質使用障礙的成人 ADHD（開放性研究） |
| [NCT00000268](https://clinicaltrials.gov/study/NCT00000268) | 不適用 | 完成 | 32 | 古柯鹼濫用合併注意力不足障礙，樣本小且年代較早 |
| [NCT04553263](https://clinicaltrials.gov/study/NCT04553263) | Early Phase 1 | 撤回 | 0 | 興奮劑使用障礙的復發預防，未實際收案，無證據價值 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28965364](https://pubmed.ncbi.nlm.nih.gov/28965364/) | 2017 | 系統性回顧 (Cochrane) | Cochrane Database Syst Rev | 評估 Bupropion 用於成人 ADHD，作為興奮劑無效或無法耐受時的替代選項 |
| [30097390](https://pubmed.ncbi.nlm.nih.gov/30097390/) | 2018 | 系統性回顧／網絡統合分析 | Lancet Psychiatry | 比較兒童、青少年與成人 ADHD 藥物的療效與耐受性 |
| [33085721](https://pubmed.ncbi.nlm.nih.gov/33085721/) | 2020 | 系統性回顧／網絡統合分析 | PLoS One | 比較成人 ADHD 各藥物治療的相對效果 |
| [27738872](https://pubmed.ncbi.nlm.nih.gov/27738872/) | 2017 | 多重治療比較 | Mol Neurobiol | 評估兒童與青少年 ADHD 藥物的療效與安全性 |
| [37405312](https://pubmed.ncbi.nlm.nih.gov/37405312/) | 2023 | Review | Health Psychol Res | 回顧 Bupropion 的藥動、藥效與作用機轉，涵蓋憂鬱症、ADHD 與戒菸 |
| [38915262](https://pubmed.ncbi.nlm.nih.gov/38915262/) | 2024 | Review | Expert Rev Neurother | 成人 ADHD 非興奮劑藥物回顧 |
| [39172673](https://pubmed.ncbi.nlm.nih.gov/39172673/) | 2024 | Review | Am Fam Physician | 成人 ADHD 的診斷與治療總覽 |
| [26601963](https://pubmed.ncbi.nlm.nih.gov/26601963/) | 2016 | Review | Curr Pharm Des | ADHD 藥物的效果與副作用，提及 Bupropion 為常用藥物之一 |
| [17136226](https://pubmed.ncbi.nlm.nih.gov/17136226/) | 2006 | Review | Drugs Today | Bupropion 概述，主要機轉為多巴胺與去甲腎上腺素再回收抑制 |
| [24259638](https://pubmed.ncbi.nlm.nih.gov/24259638/) | 2014 | Review | Ann Pharmacother | ADHD 的病理生理、病因與治療回顧 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-58371 | WELLBUTRIN XL EXTENDED RELEASE TAB 150MG | 延長釋放錠 | 未載明 |
| HK-58253 | WELLBUTRIN XL EXTENDED RELEASE TAB 300 MG | 延長釋放錠 | 未載明 |
| HK-58534 | PMS-BUPROPION SR TAB 150MG | 持續釋放錠 | 未載明 |
| HK-68758 | NEUROTRAX SUSTAINED-RELEASE TABLETS 150MG | 持續釋放錠 | 未載明 |
| HK-65953 | BUPROPION HYDROCHLORIDE SUSTAINED-RELEASE TABLETS 150MG | 持續釋放錠 | 未載明 |

另有 1 張許可證 HK-66934（CONTRAVE PROLONGED-RELEASE TABLETS 8MG/90MG），為與 naltrexone 的組合製劑品名，登記為單方許可證。

---

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆潛在交互作用，主要的重大 (Major) 等級包括：Fentanyl、Lidocaine、Dihydrocodeine、Codeine、Tramadol、Methylphenidate、Hydrocortisone、Aldesleukin、Alfentanil、Amantadine。中度 (Moderate) 等級包括 Alprazolam、Nifedipine、Hydrochlorothiazide、Cetirizine、Ethanol 等。Bupropion 對 CYP2D6 有抑制作用，因此合併用藥負擔大。
- **知識圖譜標示的禁忌或需謹慎情況**（來自知識圖譜，非仿單內容）：癲癇、高血壓、肝衰竭與肝硬化、腎臟疾病、躁狂型雙相情感障礙、精神病性疾患、厭食症與暴食症、物質濫用或依賴、心肌梗塞、中樞神經系統腫瘤等。
- **推進時需留意的風險**：癲癇風險（與劑量相關）、血壓監測，以及物質使用或飲食障礙患者需特別謹慎。

仿單的正式警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有 1 個已完成的 Phase 3 安慰劑對照 RCT（成人 ADHD，n=162），另有多個 Phase 2/3/4 試驗與 Cochrane 等系統性回顧支持，且機轉（多巴胺／去甲腎上腺素再回收抑制）合理。
- Bupropion 在香港已上市，但癲癇風險與大量藥物交互作用需要明確的防護措施。

**若要推進需要：**
- 取得香港仿單的警語與禁忌資料，完成安全性篩選。
- 確認 NCT00048360 的主要結果與比較組細節，並評估是否有第二個 Phase 3 RCT 可支持 L1。
- 訂定癲癇風險、血壓監測，以及物質使用與飲食障礙族群的用藥篩選計畫。
- 建立合併用藥（尤其是 CYP2D6 受質、鴉片類藥物與 methylphenidate）的審查機制。
- 確認香港許可證的核准適應症文字，評估是否需申請新增 ADHD 適應症。

---

## 其他預測適應症的簡要評估

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|-----|-----------|-----------|---------|------|
| 2 | ADHD，注意力不足型 | 99.99% | L3 | 研究問題（屬 ADHD 亞型，可由主要 ADHD 試驗推導，僅有間接的事後分析） |
| 3 | Faciodigitogenital syndrome | 99.98% | L5 | Hold（無機轉與證據） |
| 4 | 特定發展障礙 | 99.97% | L4 | Hold（文獻與疾病治療無直接關聯） |
| 5 | Chondromyxoid fibroma | 99.96% | L5 | Hold（無合理機轉） |
| 6 | 16p11.2 近端微缺失症候群 | 99.75% | L5 | Hold（僅有神經發展特徵的間接關聯） |
| 7–10 | 維生素過多症、嬰兒良性陣發性斜頸、三叉神經腫瘤、眼距過寬 | 99.30%–99.69% | L5 | Hold（無合理機轉或證據；嬰兒良性陣發性斜頸另有癲癇閾值的安全疑慮） |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

