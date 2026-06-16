---
layout: default
title: Clioquinol
parent: 中證據等級 (L3-L4)
nav_order: 180
evidence_level: L3
indication_count: 7
---

# Clioquinol
{: .fs-9 }

證據等級: **L3** | 預測適應症: **7** 個
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

# Clioquinol：從外用皮膚感染症到皮膚念珠菌病

## 一句話總結

Clioquinol（氯碘羥喹）是一種鹵化 8-羥基喹啉衍生物，歷史上以 Vioform 等外用製劑廣泛用於皮膚感染症的治療。
TxGNN 模型預測它可能對**皮膚念珠菌病 (Cutaneous Candidiasis)** 有效，
目前有 **6 篇文獻**（均為 1965–1988 年歷史臨床評估）支持這個方向，且無登記中的臨床試驗。
值得注意的是，此預測本質上屬於**歷史適應症的恢復**，而非全新再利用發現。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 外用皮膚感染症（歷史製劑 Vioform / Locacorten-Vioform 用途） |
| 預測新適應症 | 皮膚念珠菌病 (Cutaneous Candidiasis) |
| TxGNN 預測分數 | 99.84% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

**作用機轉（MOA）**：DrugBank 詳細 MOA 資料目前尚缺，但根據已知藥理特性，Clioquinol 透過**金屬離子螯合作用**發揮抗真菌效果——特異性螯合 Zn²⁺、Cu²⁺ 和 Fe³⁺，從而抑制念珠菌等真菌賴以維生的金屬依賴性酵素系統，並同步破壞真菌細胞膜的完整性，對表淺皮膚念珠菌感染具有直接作用位點。

**原適應症與新適應症的關聯性**：Clioquinol 的歷史使用記錄直接支持此預測。歷史製劑 Locacorten-Vioform（含 clioquinol 3% + flumethasone 0.02%）在多個國家曾被正式核准用於皮膚念珠菌病及繼發性感染皮膚病的治療。現有文獻（如 1975 年 430 例雙盲研究、1979 年 80 例平行比較試驗）均直接記錄了含 clioquinol 製劑對皮膚念珠菌感染的臨床療效。**此案例本質上是歷史適應症的恢復，而非純粹新發現的再利用方向。**

**機轉適用性**：外用途徑可最大程度降低系統性毒性風險（包括曾引發嚴重爭議的 SMON 神經毒性）。現代外用配方技術可進一步優化皮膚滲透性與局部藥物濃度，為歷史用途的現代化重建提供可行基礎。2021 年研究亦確認 clioquinol 與 ciclopirox、terbinafine 聯合用藥具有協同抗真菌活性，顯示其現代應用潛力不限於單藥使用。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [155507](https://pubmed.ncbi.nlm.nih.gov/155507/) | 1979 | Clinical Evaluation | Current Medical Research and Opinion | HNA 乳霜 vs. iodochlorhydroxyquin-HC 治療皮膚念珠菌病：整體優異療效 95% vs. 43%（共 80 例） |
| [6459255](https://pubmed.ncbi.nlm.nih.gov/6459255/) | 1981 | Comparative Clinical Study | Journal of International Medical Research | 154 名患者隨機平行比較研究（含 67 名皮膚念珠菌病），含 iodochlorhydroxyquin 的 BGI 複方與 HNN 複方整體療效相當 |
| [128475](https://pubmed.ncbi.nlm.nih.gov/128475/) | 1975 | Prospective Clinical Evaluation | Dermatologica | 430 名患者雙盲研究：Locacorten（0.02%）-Vioform（3%）複方在繼發性感染皮膚病的微生物轉陰及臨床改善，顯著優於單用 Vioform 或 Locacorten |
| [136333](https://pubmed.ncbi.nlm.nih.gov/136333/) | 1976 | Clinical Evaluation | Current Therapeutic Research | 含 halcinonide 與 iodochlorhydroxyquin 的新型抗真菌複方臨床評估 |
| [4220930](https://pubmed.ncbi.nlm.nih.gov/4220930/) | 1965 | Case Series / Observational | Zeitschrift fur Haut | 探討酵母菌在腸病性肢端皮炎（Danbolt-Closs acrodermatitis enteropathica）病因中的角色，涉及 clioquinol 治療背景 |
| [2978600](https://pubmed.ncbi.nlm.nih.gov/2978600/) | 1988 | Observational / Prevention Study | Przeglad dermatologiczny | 體外研究：多種肥皂添加物對白色念珠菌菌株的殺菌效果，強鹼性皂液中 clioquinol 展現最強殺真菌活性 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ **重要背景說明**：根據現有藥理文獻及 `predicted_indications` 的機轉分析，Clioquinol **系統性使用（口服）**曾與日本 SMON（亞急性脊髓視神經病變）群聚事件相關，多國因此限制或撤回其口服製劑。本預測指向的**外用局部製劑**之安全性資料相對有利，但詳細警語、禁忌及當前法規狀態請查閱原廠說明書或向相關藥監機關確認。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Clioquinol 用於皮膚念珠菌病屬於歷史適應症的現代恢復，有 L3 等級的歷史臨床觀察性研究支持，歷史製劑 Locacorten-Vioform 亦有實際使用先例可稽；限定**外用局部途徑**可有效規避系統性 SMON 毒性的關鍵安全疑慮，可行性基礎明確。

**若要推進需要：**
- 查閱 DrugBank API 補齊完整 MOA 資料及藥理分類
- 下載並解析原廠仿單 PDF，補充 TFDA 警語與禁忌資料（目前均為資料缺口）
- 委託現代化外用配方設計與皮膚滲透性（Franz cell 等）研究
- 針對當代臨床念珠菌分離株進行體外抗真菌活性確認試驗（含 MIC 測定）
- 系統性文獻回顧，聚焦外用 clioquinol 的安全性與現代臨床應用資料
- 評估香港藥監法規路徑：是否以現有製劑（仿製或進口）申請許可，抑或需全新配方開發
- 探索與 ciclopirox、terbinafine 等現行外用抗真菌藥的聯合用藥協同效應（2021 年體外數據提供初步依據）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

