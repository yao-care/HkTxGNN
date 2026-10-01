---
layout: default
title: Vilanterol
parent: 高證據等級 (L1-L2)
nav_order: 919
evidence_level: L1
indication_count: 5
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

<div id="pharmacist">

## 藥師評估報告

</div>

# Vilanterol：從長效 β2 支氣管擴張劑到阻塞性肺病

## 一句話總結

Vilanterol 是長效 β2 受體促效劑（LABA），主要以複方吸入劑形式使用（如 FF/VI、UMEC/VI、FF/UMEC/VI）。
TxGNN 模型預測它可能對**阻塞性肺病 (Obstructive Lung Disease)** 有效，目前有 **46 個臨床試驗**和 **20 篇文獻**支持，其中多項為已完成的 Phase 3 RCT。
不過這個預測與其現有用途（COPD 維持治療）高度重疊，更接近**既有適應症的確認**，而非真正的老藥新用。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 來源資料未提供（許可證適應症欄位為空） |
| 預測新適應症 | 阻塞性肺病 (Obstructive Lung Disease) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。依藥理類別，Vilanterol 是長效 β2 腎上腺素受體促效劑，透過 β2 受體／cAMP 路徑使氣道平滑肌鬆弛，直接針對 COPD 的氣流受限。

阻塞性肺病的核心問題是氣流阻塞，支氣管擴張劑正是對應這個病理環節的藥物。多項 Phase 3 RCT 已證實含 Vilanterol 的複方（FF/VI、UMEC/VI、FF/UMEC/VI）可改善肺功能與健康狀態。因此預測在機轉與臨床上都說得通。

有兩點需要注意：
- 現有證據幾乎都來自**複方**試驗，Vilanterol 單獨的貢獻無法單獨分離。
- 此藥已在 COPD 使用，原適應症欄位為空，很可能是來源資料缺漏，而非真的沒有適應症。

---

## 臨床試驗證據

共檢索到 46 個試驗，以下列出 10 個最相關者。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01313676](https://clinicaltrials.gov/study/NCT01313676) | Phase 3 | 完成 | 16568 | FF/VI 對比安慰劑，評估中度 COPD 且有心血管風險患者的存活率 |
| [NCT02345161](https://clinicaltrials.gov/study/NCT02345161) | Phase 3 | 完成 | 1811 | FF/UMEC/VI 對比 budesonide/formoterol，24 週肺功能與健康狀態 |
| [NCT01316913](https://clinicaltrials.gov/study/NCT01316913) | Phase 3 | 完成 | 872 | UMEC/VI 對比 UMEC 單方及 tiotropium，24 週療效與安全性 |
| [NCT02729051](https://clinicaltrials.gov/study/NCT02729051) | Phase 3 | 完成 | 1055 | 單一吸入器三合一療法與 FF/VI + UMEC 開放式三合一療法比較，24 週 |
| [NCT01336608](https://clinicaltrials.gov/study/NCT01336608) | Phase 3 | 完成 | 446 | FF/VI 對 COPD 患者動脈硬度的影響，24 週 |
| [NCT02105974](https://clinicaltrials.gov/study/NCT02105974) | Phase 3 | 完成 | 1621 | FF/VI 對比 VI 單方，評估 FF 對肺功能的貢獻，12 週 |
| [NCT01323634](https://clinicaltrials.gov/study/NCT01323634) | Phase 3 | 完成 | 519 | FF/VI 對比 fluticasone propionate/salmeterol，24 小時肺功能 |
| [NCT01822899](https://clinicaltrials.gov/study/NCT01822899) | Phase 3 | 完成 | 717 | UMEC/VI 對比 fluticasone propionate/salmeterol，12 週 |
| [NCT02152605](https://clinicaltrials.gov/study/NCT02152605) | Phase 3 | 完成 | 498 | UMEC/VI 對比安慰劑，生活品質與症狀，12 週 |
| [NCT03474081](https://clinicaltrials.gov/study/NCT03474081) | Phase 4 | 完成 | 800 | 單一吸入器三合一療法對比 tiotropium 單方，12 週 |

另有多項氣喘（asthma）試驗，如 NCT02924688（n=2436）和 NCT01686633（n=1040）。這些屬於不同適應症，此處不列入。

---

## 文獻證據

共檢索到 20 篇文獻，以下列出 10 篇（RCT 與其事後分析優先，其次為統合分析與觀察性研究）。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29668352](https://pubmed.ncbi.nlm.nih.gov/29668352/) | 2018 | RCT | N Engl J Med | IMPACT 試驗：每日一次單一吸入器三合一療法與雙重療法比較 |
| [32918892](https://pubmed.ncbi.nlm.nih.gov/32918892/) | 2021 | RCT | Lancet Respir Med | CAPTAIN 試驗：FF/UMEC/VI 對比 FF/VI 用於控制不佳的氣喘 |
| [28375647](https://pubmed.ncbi.nlm.nih.gov/28375647/) | 2017 | 試驗摘要 | Am J Respir Crit Care Med | FULFIL 試驗：三合一療法對比 ICS/LABA 雙重療法 |
| [32162970](https://pubmed.ncbi.nlm.nih.gov/32162970/) | 2020 | RCT 事後分析 | Am J Respir Crit Care Med | FF/UMEC/VI 相較 UMEC/VI 降低全因死亡率 |
| [31281061](https://pubmed.ncbi.nlm.nih.gov/31281061/) | 2019 | RCT 事後分析 | Lancet Respir Med | 血中嗜酸性球數與三合一／雙重療法療效的關係 |
| [39696097](https://pubmed.ncbi.nlm.nih.gov/39696097/) | 2024 | 統合分析 | BMC Pulm Med | UMEC/VI 與其他支氣管擴張劑的療效比較 |
| [35849317](https://pubmed.ncbi.nlm.nih.gov/35849317/) | 2022 | 網絡統合分析 | Adv Ther | FF/UMEC/VI 與其他三合一及雙重療法的療效比較 |
| [29094315](https://pubmed.ncbi.nlm.nih.gov/29094315/) | 2017 | 隨機研究 | Adv Ther | UMEC/VI 與 tiotropium/olodaterol 的首次直接比較 |
| [39797646](https://pubmed.ncbi.nlm.nih.gov/39797646/) | 2024 | 世代研究 | BMJ | 兩種單一吸入器三合一療法的真實世界療效與安全性比較 |
| [28956463](https://pubmed.ncbi.nlm.nih.gov/28956463/) | 2017 | 回顧 | Expert Rev Respir Med | FF/VI 用於穩定期 COPD 的角色 |

---

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-62693 | RELVAR ELLIPTA 吸入粉劑 100/25 mcg | GlaxoSmithKline Limited |
| HK-62694 | RELVAR ELLIPTA 吸入粉劑 200/25 mcg | GlaxoSmithKline Limited |
| HK-63414 | ANORO ELLIPTA 吸入粉劑 62.5/25 mcg | GlaxoSmithKline Limited |
| HK-65911 | TRELEGY ELLIPTA 吸入粉劑 100/62.5/25 mcg | GlaxoSmithKline Limited |
| HK-67942 | TRELEGY ELLIPTA 吸入粉劑 200/62.5/25 mcg | GlaxoSmithKline Limited |

資料中未提供核准適應症文字，需另行向衞生署查證。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
有多項已完成的 Phase 3 RCT（含 16,568 人的存活率研究）與高品質文獻支持含 Vilanterol 的複方用於 COPD，證據等級為 L1，且已在香港上市。但這屬於既有用途，證據來自複方，且安全性資料有缺口，因此以附帶條件方式推進。

**若要推進需要：**
- 向衞生署查證各許可證的核准適應症，確認 COPD 是否已在標示內，並注意氣喘適應症具地區差異
- 取得香港仿單的警語與禁忌症
- 補充 DrugBank 的作用機轉資料
- 釐清 Vilanterol 單獨的貢獻，目前證據多為複方試驗

另外，排名第 2 至 5 的預測（間質性肺氣腫、代償性肺氣腫、透亮肺、氣管狹窄）目前證據不足或缺乏機轉依據，建議全部 **Hold**。

*本報告僅供研究參考，不構成醫療建議，老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

