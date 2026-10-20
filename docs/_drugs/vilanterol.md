---
layout: default
title: Vilanterol
parent: 高證據等級 (L1-L2)
nav_order: 934
evidence_level: L1
indication_count: 5
last_modified_at: 2026-10-14
description: "Vilanterol：預測新適應症為阻塞性肺病 (Obstructive Lung Disease)（證據等級 L1）。原適應症：慢性阻塞性肺病、支氣管炎、氣喘、肺氣腫"
monitor_inn: "VILANTEROL"
predicted_indications: ["hyperlucent lung", "tracheal stenosis"]
---

# Vilanterol
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
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

# Vilanterol：從慢性阻塞性肺病與氣喘到阻塞性肺病

## 一句話總結

Vilanterol 是一種長效 β2 受體促效劑（LABA），原本用於慢性阻塞性肺病（COPD）、氣喘等呼吸道疾病的維持治療。
TxGNN 模型預測它可能對**阻塞性肺病 (Obstructive Lung Disease)** 有效，
目前有 **27 個臨床試驗**和 **20 篇文獻**支持這個方向。
需注意：阻塞性肺病涵蓋 COPD 與氣喘，本質上屬於原有適應症的範圍，並非真正的新用途。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性阻塞性肺病、支氣管炎、氣喘、肺氣腫（取自知識圖譜；香港許可證未提供適應症文字） |
| 預測新適應症 | 阻塞性肺病 (Obstructive Lung Disease) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據藥物類別，Vilanterol 是長效 β2 腎上腺素受體促效劑，
透過 cAMP 路徑使氣道平滑肌鬆弛而擴張支氣管。此說明是依該類藥物的已知藥理推論，並非來自資料庫的 MOA 欄位。

「阻塞性肺病」是涵蓋 COPD 與氣喘的上位疾病類別，而這兩者正是 Vilanterol 已知的適應症。
因此這個預測屬於**既有適應症的符合**，高分（99.97%）與此一致，不應視為真正的藥物再利用發現。

Vilanterol 在臨床上多以複方吸入劑使用，例如與 fluticasone furoate（ICS）、umeclidinium（LAMA）合用，下列證據多來自這些複方。

另外，模型也預測了其他幾個較不明確的適應症（間質性肺氣腫、代償性肺氣腫、透亮肺、氣管狹窄），
這些皆僅有模型預測，沒有任何臨床試驗或文獻，且機轉上缺乏支持（例如氣管狹窄屬固定的結構性狹窄，支氣管擴張劑預期無法改善），
很可能是知識圖譜中與 COPD／肺氣腫節點相鄰所造成的假象。

---

## 臨床試驗證據

資料共 27 個試驗，以下列出最相關的 10 個：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05062304](https://clinicaltrials.gov/study/NCT05062304) | N/A（IMPACT 試驗） | 完成 | 17,281 | 每日一次單一吸入器三合一療法（FF/UMEC/VI）對比雙重療法用於 COPD |
| [NCT03162055](https://clinicaltrials.gov/study/NCT03162055) | Phase 3 | 完成 | 1,119 | 雙盲 RCT，比較 glycopyrronium/formoterol 與 umeclidinium/vilanterol，24 週，中重度 COPD |
| [NCT01686633](https://clinicaltrials.gov/study/NCT01686633) | Phase 3 | 完成 | 1,040 | FF/VI 200/25 與 100/25 對比 FF 100，用於中重度持續性氣喘 |
| [NCT01134042](https://clinicaltrials.gov/study/NCT01134042) | Phase 3 | 完成 | 587 | FF/VI 對比 FF 單方與 FP，24 週，持續性氣喘 |
| [NCT02094937](https://clinicaltrials.gov/study/NCT02094937) | Phase 3 | 完成 | 430 | 日本氣喘患者由 FF/VI 降階至 FF 或 FP 的療效與安全性比較 |
| [NCT01777334](https://clinicaltrials.gov/study/NCT01777334) | Phase 3 | 完成 | 905 | UMEC/VI 對比 tiotropium，24 週，COPD 的谷值 FEV1 |
| [NCT01342913](https://clinicaltrials.gov/study/NCT01342913) | Phase 3 | 完成 | 528 | FF/VI 每日一次對比 salmeterol/FP 每日兩次，COPD 的 24 小時肺功能 |
| [NCT02301975](https://clinicaltrials.gov/study/NCT02301975) | Phase 3 | 完成 | 1,526 | FF/VI 對比 FP/salmeterol 及 FP 的非劣性試驗，氣喘 |
| [NCT01706198](https://clinicaltrials.gov/study/NCT01706198) | Phase 3 | 完成 | 4,233 | 12 個月開放標籤實效性研究，FF/VI 對比常規維持療法，氣喘 |
| [NCT04265105](https://clinicaltrials.gov/study/NCT04265105) | Phase 2/3 | 完成 | 18 | 輕度氣喘成人使用 fluticasone-vilanterol 的小型先導 RCT |

---

## 文獻證據

資料共 20 篇，以下依 RCT > 系統性回顧／統合分析 > 其他研究 排序，列出 10 篇：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29668352](https://pubmed.ncbi.nlm.nih.gov/29668352/) | 2018 | RCT | N Engl J Med | IMPACT：單一吸入器三合一療法與雙重療法於 COPD 的比較 |
| [28375647](https://pubmed.ncbi.nlm.nih.gov/28375647/) | 2017 | RCT | Am J Respir Crit Care Med | FULFIL：每日一次三合一療法對比 ICS/LABA 雙重療法 |
| [32918892](https://pubmed.ncbi.nlm.nih.gov/32918892/) | 2021 | RCT（Phase 3A） | Lancet Respir Med | CAPTAIN：FF/UMEC/VI 與 FF/VI 用於控制不佳的氣喘 |
| [32162970](https://pubmed.ncbi.nlm.nih.gov/32162970/) | 2020 | RCT 事後／合併分析 | Am J Respir Crit Care Med | IMPACT 追蹤分析：FF/UMEC/VI 降低 COPD 全因死亡率 |
| [35849317](https://pubmed.ncbi.nlm.nih.gov/35849317/) | 2022 | 網絡統合分析 | Adv Ther | FF/UMEC/VI 與其他三合一及雙重療法的療效比較 |
| [39696097](https://pubmed.ncbi.nlm.nih.gov/39696097/) | 2024 | 系統性回顧與統合分析 | BMC Pulm Med | UMEC/VI 與其他支氣管擴張劑於 COPD 的療效比較 |
| [31389190](https://pubmed.ncbi.nlm.nih.gov/31389190/) | 2019 | 系統性回顧 | Clin Respir J | UMEC/VI 固定複方用於 COPD 的系統性回顧 |
| [39797646](https://pubmed.ncbi.nlm.nih.gov/39797646/) | 2024 | 世代研究 | BMJ | 兩種單一吸入器三合一療法於真實世界的療效與安全性比較 |
| [39731707](https://pubmed.ncbi.nlm.nih.gov/39731707/) | 2025 | 世代研究（真實世界） | Adv Ther | FF/UMEC/VI 與 BUD/GLY/FORM 於美國 COPD 患者的比較 |
| [40619503](https://pubmed.ncbi.nlm.nih.gov/40619503/) | 2025 | 世代研究（真實世界） | Adv Ther | 由雙重療法升階的 COPD 患者中兩種三合一療法的比較 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-62693 | RELVAR ELLIPTA 吸入粉劑 100MCG/25MCG | 吸入粉劑 | — |
| HK-62694 | RELVAR ELLIPTA 吸入粉劑 200MCG/25MCG | 吸入粉劑 | — |
| HK-63414 | ANORO ELLIPTA 吸入粉劑 62.5MCG/25MCG | 吸入粉劑 | — |
| HK-65911 | TRELEGY ELLIPTA 吸入粉劑 100MCG/62.5MCG/25MCG | 吸入粉劑 | — |
| HK-67942 | TRELEGY ELLIPTA 吸入粉劑 200MCG/62.5MCG/25MCG | 吸入粉劑 | — |

以上 5 張許可證均為有效狀態，持有者為 GlaxoSmithKline Limited。許可證資料中未提供適應症文字與劑型欄位，品名所示劑型為吸入粉劑。

---

## 安全性考量

- **藥物交互作用**：資料庫共記錄 100 筆交互作用，以下為部分主要項目：
  - 中度：抗糖尿病藥物（acarbose、albiglutide、alogliptin、canagliflozin、dapagliflozin、empagliflozin、dulaglutide、chlorpropamide）、cisapride、clarithromycin、dolasetron、diethylpropion、ephedrine、epinephrine
  - 輕度：皮質類固醇（beclomethasone、betamethasone、budesonide、dexamethasone）

主要警語與禁忌症資料缺乏，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有多個完成的 Phase 3 RCT（如 IMPACT、FULFIL、CAPTAIN 等）支持含 Vilanterol 的複方用於 COPD 與氣喘，且香港已有 5 張有效許可證。但此預測實為既有適應症的符合，並非新的再利用方向；證據多來自複方，無法單獨歸因於 Vilanterol。
- 其餘預測適應症（間質性肺氣腫、代償性肺氣腫、透亮肺、氣管狹窄）僅有模型預測、缺乏證據且機轉不合理，建議維持 Hold。

**若要推進需要：**
- 取得香港仿單的警語、禁忌症與核准適應症文字（目前缺乏，屬阻礙性資料缺口）
- 補充詳細的作用機轉（MOA）資料
- 釐清此預測是否有超出既有適應症的實質價值，以決定是否值得投入再利用評估
- 針對 DDI 清單中的中度交互作用（如併用糖尿病藥物、clarithromycin、擬交感神經藥物）建立監測與用藥指引
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

