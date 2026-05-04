---
layout: default
title: Diazepam
parent: 高證據等級 (L1-L2)
nav_order: 200
evidence_level: L1
indication_count: 10
---

# Diazepam
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Diazepam：從焦慮症到失眠

## 一句話總結

Diazepam（安定/Valium）是廣泛使用的苯二氮平類藥物，國際上已核准用於焦慮症、肌肉痙攣及癲癇等適應症，惟香港目前並無正式上市許可。TxGNN 模型預測它可能對**失眠 (Insomnia)** 有效，目前有 **24 個臨床試驗**和 **18 篇文獻**支持這個方向。需注意長期使用存在耐受性、依賴性及認知損害等顯著安全疑慮。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 焦慮症、肌肉痙攣、癲癇（國際核准用途；香港無核准許可證） |
| 預測新適應症 | 失眠 (Insomnia) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Diazepam 是 GABA-A 受體的**正性變構調節劑（Positive Allosteric Modulator, PAM）**。它與 GABA-A 受體上的苯二氮平結合位點作用，增強氯離子通道的開放頻率，強化 GABAergic 抑制傳導，從而產生鎮靜催眠、抗焦慮及肌肉鬆弛等效果。

失眠的核心問題在於睡眠啟動困難（sleep-onset insomnia）及睡眠維持困難（sleep-maintenance insomnia）。Diazepam 透過增強中樞神經抑制傳導，可直接縮短入睡潛伏期並延長睡眠持續時間，藥理機轉上與失眠治療高度契合——1981 年的 RCT 已直接比較 Diazepam 與其他 BZD 類安眠藥在失眠患者中的療效（PMID 6113175）。

然而，現有大量文獻揭示 Diazepam 長期用於失眠的重大限制：耐受性（efficacy diminishes over time）、生理及心理依賴性，以及認知損害風險——研究顯示長期使用可透過粒線體 18kDa 轉位蛋白（TSPO）途徑增強微膠細胞突觸吞噬，導致持久性認知功能下降（PMID 35228700）。現代臨床指引已明確建議以認知行為療法（CBTI）及選擇性更強的新型藥物（如雙 orexin 受體拮抗劑）取代傳統苯二氮平類藥物作為慢性失眠的第一線治療。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02831894](https://clinicaltrials.gov/study/NCT02831894) | Phase 2 | 完成 | 74 | 評估 BZD（含 Diazepam）漸進減藥速率與個體特質的交互作用，確認失眠族群的 BZD 高度依賴現象 |
| [NCT04050176](https://clinicaltrials.gov/study/NCT04050176) | Phase 3 | 進行中（停止招募） | 260 | 評估盲化漸進減藥合併 CBTI 對催眠藥（含 BZD）依賴失眠患者的戒斷效果，RCT 設計 |
| [NCT03461042](https://clinicaltrials.gov/study/NCT03461042) | Phase 4 | 完成 | 17 | 雙盲安慰劑對照試驗，評估 Ramelteon 輔助慢性失眠患者 BZD 減藥的效果 |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | 觀察性 | 未知 | 1,400 | 台灣前瞻性研究，評估老年失眠患者使用催眠藥（含 Diazepam）之風險效益及藥物動力學特性 |
| [NCT03687086](https://clinicaltrials.gov/study/NCT03687086) | 非干預性 | 完成 | 188 | 老年族群催眠藥減藥介入研究，評估新型機制促進長期停用催眠藥的可行性 |
| [NCT04751851](https://clinicaltrials.gov/study/NCT04751851) | 非干預性 | 完成 | 128 | 評估接受與承諾療法（ACT）合併減藥計畫對 BZD 依賴失眠患者的戒斷效果，遠距心理治療介入 |
| [NCT04364321](https://clinicaltrials.gov/study/NCT04364321) | 非分期 | 未知 | 74 | 直接比較單次 Clonazepam 與間歇性口服 Diazepam 預防兒童反覆發燒性痙攣，佐證 Diazepam 之 CNS 抑制效果 |
| [NCT02530580](https://clinicaltrials.gov/study/NCT02530580) | Phase 1 | 完成 | 12 | 評估選擇性 GABA 調節劑（以 Diazepam 為陽性對照），直接確認 BZD 類藥物在失眠相關神經調節的作用機轉 |
| [NCT07417813](https://clinicaltrials.gov/study/NCT07417813) | 觀察性 | 招募中 | 121 | 評估新型雙 orexin 受體拮抗劑 Lemborexant 取代 BZD（含 Diazepam）治療精神疾病合併失眠的效果 |
| [NCT02281175](https://clinicaltrials.gov/study/NCT02281175) | 非干預性 | 完成 | 114 | 評估針對老年 BZD 使用者的心理社會介入計畫（PASSE-65+）促進漸進減藥之效果，BZD 依賴失眠直接相關 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [6113175](https://pubmed.ncbi.nlm.nih.gov/6113175/) | 1981 | RCT | J Int Med Res | 100 名失眠患者雙盲試驗：Lormetazepam 1mg vs **Diazepam 5mg**，Lormetazepam 在縮短入睡時間及延長睡眠持續時間均優於 Diazepam（p<0.05） |
| [39374004](https://pubmed.ncbi.nlm.nih.gov/39374004/) | 2024 | RCT | JAMA Intern Med | 盲化 BZD 漸進減藥合併 CBTI 之 RCT，揭示安慰劑效應在 BZD 減藥過程中的重要角色，支持 CBTI 優先於 BZD 的治療策略 |
| [40570297](https://pubmed.ncbi.nlm.nih.gov/40570297/) | 2025 | 世代研究 | Sleep | 慢性 BZD/BZRA 使用破壞老年失眠患者的睡眠巨觀架構及 NREM 慢波振盪－睡眠紡錘波耦合，損害記憶鞏固功能 |
| [39581171](https://pubmed.ncbi.nlm.nih.gov/39581171/) | 2024 | Review | Bioorg Chem | GABA-A 受體小分子調節劑（含 Diazepam）在失眠、癲癇、焦慮等神經系統疾病的臨床應用及安全性綜述 |
| [35228700](https://pubmed.ncbi.nlm.nih.gov/35228700/) | 2022 | 基礎/轉譯 | Nature Neurosci | 長期 Diazepam 使用透過 TSPO 途徑增強微膠細胞突觸吞噬，損害樹突棘結構可塑性，導致持久性認知損害 |
| [7595266](https://pubmed.ncbi.nlm.nih.gov/7595266/) | 1995 | Review | J Fam Pract | 系統性回顧老年社區失眠者使用 BZD 之效益與風險：短期有效，但跌倒、骨折風險顯著增加，不建議長期使用 |
| [7525193](https://pubmed.ncbi.nlm.nih.gov/7525193/) | 1994 | 臨床指引 | Drugs | BZD 合理使用指南：失眠以短期或間歇性使用為原則；Diazepam 屬長效型，老年人易有藥物蓄積問題 |
| [6135990](https://pubmed.ncbi.nlm.nih.gov/6135990/) | 1983 | Review | NEJM | 苯二氮平類藥物現狀之 NEJM 經典綜述，確立 BZD（含 Diazepam）在失眠及焦慮治療中的地位與限制 |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-analysis | Acta Pharm Zagreb | 評估不同鎮靜安眠藥物在老年慢性病患者的效果與不良反應，提供安全可接受的最適劑量依據 |
| [40921193](https://pubmed.ncbi.nlm.nih.gov/40921193/) | 2025 | 世代研究 | Neuropsychopharm Rep | 睡眠藥物處方集實施後 BZD 用藥模式改變：BZD 使用量下降，新型藥物取代 Diazepam 的臨床成效分析 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Diazepam 的 GABA-A 受體調節機轉提供充分的藥理學依據，且 RCT 及大型觀察性研究均確認其在失眠治療中的既有使用基礎（證據等級 L1）；然而，現代臨床指引已明確建議以 CBTI 或新型選擇性藥物取代 BZD 作為優先選擇，且香港目前無核准上市許可，進一步推進需先解決監管層面的問題。

**若要推進需要：**
- 評估在香港申請 Diazepam 上市許可的可行性及必要性
- 取得完整 Diazepam 藥品安全資訊（原廠仿單警語、禁忌症）
- 明確定義目標適應症範圍：短期／情境性失眠（較具合理性）vs 慢性失眠（安全性疑慮高）
- 制定長期使用安全監測計畫，包含認知功能評估（MMSE/MoCA）、依賴性篩查及跌倒風險評估
- 考慮以輔助短期橋接角色定位（配合 CBTI），而非單獨作為慢性失眠長期治療
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

