---
layout: default
title: Alectinib
parent: 僅模型預測 (L5)
nav_order: 29
evidence_level: L5
indication_count: 10
---

# Alectinib
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

# Alectinib：從 ALK 陽性非小細胞肺癌到 ALK 陽性神經內分泌腫瘤

## 一句話總結

Alectinib 是第二代高選擇性 ALK 酪氨酸激酶抑制劑，全球已核准用於 ALK 陽性非小細胞肺癌（NSCLC），但香港目前尚未上市。TxGNN 模型預測其最具再利用潛力的新方向為 **ALK 陽性肺神經內分泌腫瘤**（TxGNN Rank 7），目前有 **1 個進行中籃型臨床試驗**（NCT05770037）及 **6 個以上病例報告**支持，建議列為研究探索方向（Research Question）。此外，Rank 5 預測節點具 **L1 等級證據**（4 個 Phase 3 RCT 含亞裔隊列），可同步支持香港藥品引進評估。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | ALK 陽性非小細胞肺癌（全球已核准；香港未上市） |
| 預測新適應症 | ALK 陽性神經內分泌腫瘤（TxGNN Rank 7 / Lung Germ Cell Tumor 節點） |
| TxGNN 預測分數 | 99.95%（Rank 7） |
| 證據等級 | L3（Rank 7 / ALK+ 神經內分泌腫瘤）；L1 作為背景（Rank 5 / ALK+ NSCLC） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Research Question（ALK+ 神經內分泌腫瘤再利用） |

> **⚠️ TxGNN 全局預測摘要**：本次共產出 10 個預測。**Rank 1–4**（牙齦纖維瘤病、肺纖維瘤、肺錯構瘤、肺門癌）及 **Rank 6、8–10** 均因與 ALK/RET 訊號軸無機轉交集，評為圖拓樸假陽性，建議 **Hold**。**Rank 5**（肺腫瘤節點）在知識圖譜中實際映射至 ALK+ NSCLC，承載 L1 等級 RCT 數據，建議同步考量香港引進（**Proceed with Guardrails**）。本報告聚焦 **Rank 7** 作為真正的再利用研究方向。

---

## 為什麼這個預測合理？

Alectinib 的 MOA 尚缺乏 DrugBank 正式記錄（資料缺口 DG002），根據臨床文獻可重建其藥理基礎：

**作用機轉**：Alectinib 是 ATP 競爭性 ALK 激酶抑制劑（Ki = 1.9 nM），選擇性抑制 EML4-ALK 融合蛋白的自磷酸化，阻斷下游 RAS/MAPK、PI3K/AKT 及 JAK-STAT 訊號傳導，誘導 ALK 依賴性腫瘤細胞凋亡。相較第一代抑制劑 Crizotinib，Alectinib 具更強的 CNS 穿透性，並對多種耐藥突變（如 G1202R）保留抑制活性。

**再利用合理性**：ALK 重排融合基因（EML4-ALK、KIF5B-ALK、CEP44-ALK 等）在肺大細胞神經內分泌癌（LCNEC）及非典型類癌中雖罕見（發生率 < 5%），但已確認作為致癌驅動基因存在。由於 LCNEC 缺乏有效標準治療，而 Alectinib 的 ALK 抑制機轉直接針對此分子驅動，多個真實世界病例報告已驗證其臨床療效。TxGNN 知識圖譜透過「ALK 相關肺部腫瘤節點」捕捉到此關聯，具生物學合理性。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05770037](https://clinicaltrials.gov/study/NCT05770037) | Phase 2/3 | 招募中 | 30 | DETERMINE 籃型平台試驗：評估 Alectinib 用於具 ALK 陽性基因組改變的罕見成人、兒童及青少年腫瘤；為 ALK+ 非 NSCLC 實體腫瘤提供前瞻性研究框架，結果尚待公布 |
| [NCT04644315](https://clinicaltrials.gov/study/NCT04644315) | Phase 2 | 已提前終止 | 1 | 評估 Alectinib 用於非肺癌 ALK+ 實體腫瘤；因入組困難僅收入 1 名患者即終止，不具結論性數據 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37561984](https://pubmed.ncbi.nlm.nih.gov/37561984/) | 2023 | Review | JCO Precis Oncol | 成人神經母細胞瘤中 ALK 抑制劑（含 Alectinib）的治療策略綜述；確認 ALK 突變在非 NSCLC 腫瘤的致癌驅動角色 |
| [30591488](https://pubmed.ncbi.nlm.nih.gov/30591488/) | 2019 | 回顧性研究 | Anticancer Res | 系統性評估肺 LCNEC 的 ALK 免疫組化狀態；鑑定新型 KIF5B-ALK 融合激酶，支持對 LCNEC 常規進行 ALK 篩查 |
| [36690569](https://pubmed.ncbi.nlm.nih.gov/36690569/) | 2023 | Case Report | Clin Lung Cancer | ALK 陽性肺神經內分泌腫瘤患者對 Alectinib 呈現良好臨床反應 |
| [35200571](https://pubmed.ncbi.nlm.nih.gov/35200571/) | 2022 | Case Report | Curr Oncol | IV 期 ALK 重排混合型大細胞神經內分泌癌（LCNEC）合併腺癌，骨轉移復發後接受 Alectinib 治療達部分緩解 |
| [34994612](https://pubmed.ncbi.nlm.nih.gov/34994612/) | 2021 | Case Report | JCO Precis Oncol | 轉移性 LCNEC 合併 ALK 融合基因，Alectinib 治療後腫瘤部分反應 |
| [37031440](https://pubmed.ncbi.nlm.nih.gov/37031440/) | 2023 | Case Report | Orvosi hetilap | 混合型 LCNEC 合併 ALK 融合，術後接受 Alectinib 治療；建議 ALK 陽性神經內分泌腫瘤可嘗試靶向治療取代細胞毒性化療 |
| [39667359](https://pubmed.ncbi.nlm.nih.gov/39667359/) | 2024 | Case Report | Clin Respir J | 罕見 CEP44-ALK 融合神經內分泌腫瘤對 ALK 抑制劑有顯著反應，支持 ALK-TKI 類別效果的普適性 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（第二代 ALK 酪氨酸激酶抑制劑，口服小分子）；非傳統細胞毒性化療 |
| 骨髓抑制風險 | 低（相較傳統化療，骨髓毒性顯著降低） |
| 致吐性分級 | 低度 |
| 監測項目 | CBC（含分類）、肝功能（ALT/AST/ALP/Bilirubin）、腎功能、三酸甘油酯、心電圖（QTc 及心律）、體重 |
| 處置防護 | 口服膠囊劑型，依標靶抗腫瘤藥物操作規範；特別警示嚴重高三酸甘油酯血症（可引發急性胰臟炎）及體重增加副作用 |

---

## 安全性考量

安全性資訊請參考原廠仿單（TFDA 仿單資料尚待取得，DG001 資料缺口）。

根據現有文獻已知主要安全性訊號：

- **代謝毒性**：嚴重高三酸甘油酯血症（案例報告記錄威脅生命的急性胰臟炎，需血漿置換治療）
- **皮膚反應**：DRESS 症候群（藥物超敏反應伴嗜酸性球增多及全身症狀）；多形性紅斑（個案有成功再投藥紀錄）
- **心臟電生理**：輕微 QTc 影響，無劑量依賴性 QTc 延長；需監測心動過緩
- **體重增加**：約 10% 患者出現顯著體重增加，機制尚不明確，建議定期追蹤

---

## 結論與下一步

**決策：Research Question（ALK+ 神經內分泌腫瘤再利用）**

**理由：**
ALK 重排神經內分泌腫瘤（LCNEC、非典型類癌）雖為罕見疾病，但具明確的 ALK 依賴分子機轉，多個病例報告已驗證 Alectinib 的臨床反應，且 DETERMINE 籃型試驗（NCT05770037）正在招募中，提供前瞻性評估框架。目前證據仍屬病例系列層級（L3），尚不具備直接推進大規模商業開發的依據，需等待前瞻性試驗數據。

**同步建議：Proceed with Guardrails（香港 ALK+ NSCLC 引進）**
Rank 5 節點的 L1 等級證據（ALINA、ALEX、J-ALEX、ALESIA 四個 Phase 3 RCT），尤其 ALESIA 及 J-ALEX 的亞裔隊列數據，具高度香港市場參考價值，建議同步評估向衛生署申請藥品引進。

**若要推進需要：**
- **補全安全性資料**：取得原廠完整仿單（DG001），建立 Alectinib DrugBank MOA 記錄（DG002）
- **ALK+ 神經內分泌腫瘤再利用**：持續追蹤 NCT05770037（DETERMINE）試驗結果；評估香港及亞洲地區 LCNEC 患者中 ALK 陽性率的流行病學數據；考慮病例登錄研究（registry study）積累本地數據
- **香港 ALK+ NSCLC 引進**：估算患者族群規模（約 3–5% NSCLC 攜帶 ALK 重排）；向衛生署提交特別醫療製品申請或正式新藥申請；建立 ALK 伴隨診斷（companion diagnostics）平台以確保符合精準用藥需求
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

