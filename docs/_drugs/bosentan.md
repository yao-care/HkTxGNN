---
layout: default
title: Bosentan
parent: 僅模型預測 (L5)
nav_order: 108
evidence_level: L5
indication_count: 9
---

# Bosentan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Bosentan：從肺動脈高壓到類風濕性關節炎

## 一句話總結

Bosentan 是一種雙重內皮素受體拮抗劑（ERA），原本核准用於肺動脈高壓（PAH）及全身性硬化症相關指端潰瘍的預防治療。TxGNN 模型預測它可能對**類風濕性關節炎 (Rheumatoid Arthritis)** 有效，目前有 **1 個臨床試驗**（間接相關）和 **16 篇文獻**支持這個方向，但針對 RA 患者的直接人體臨床試驗目前付之闕如，整體證據停留於動物研究與機轉推斷階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肺動脈高壓（Pulmonary Arterial Hypertension, PAH） |
| 預測新適應症 | 類風濕性關節炎 (Rheumatoid Arthritis) |
| TxGNN 預測分數 | 99.80% |
| 證據等級 | L4（動物研究與機轉研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold（研究問題） |

---

## 為什麼這個預測合理？

Bosentan 作為雙重 ETA/ETB 內皮素受體拮抗劑，其核心機轉在於阻斷內皮素-1（ET-1）對血管平滑肌及炎症細胞的作用。ET-1 在類風濕性關節炎（RA）患者的血漿及滑膜組織中顯著升高，透過 ETA/ETB 受體促進促炎細胞因子（TNF-α、IL-1β）及趨化因子（LTB4、CXCL-1）的釋放，加劇滑膜炎症、關節破壞與痛覺過敏。ET 訊號亦參與 IL-15 誘導的免疫性痛覺過敏路徑，而 IL-15 已知在 RA 病理機轉中扮演重要角色。

動物模型提供了最直接的支持證據：Bosentan 在膠原誘導性關節炎（CIA）小鼠模型中顯著降低關節炎評分並抑制 TNF-α 表達（PMID 22249931）；在酵母多糖誘導性關節炎模型中，ET-1 被確立為調控嗜中性白血球浸潤及水腫形成的關鍵媒介（PMID 18515326）；在抗原誘導性關節炎模型中，ET 訊號同樣介導 IL-17 相關的關節痛覺過敏（PMID 19969421）。這些匯聚的動物研究一致指向 ET 訊號在關節炎症路徑中的功能性角色。

然而，目前完全缺乏針對 RA 患者的直接人體臨床試驗。現有唯一相關試驗（NCT06957002）針對巨細胞動脈炎（GCA），而非 RA；兩者雖同屬風濕性疾病，但 GCA 以肉芽腫性大血管炎為主要病理，與 RA 的自體免疫性滑膜炎機轉差異顯著，證據遷移性極為有限。此外，值得特別注意的是，同批次預測中，Bosentan 用於**局限型全身性硬化症（lcSSc）指端潰瘍預防**已有 L1 等級證據（包含兩項 Phase 3 RCT：RAPIDS-1 及 RAPIDS-2），並已獲歐盟 EMA 核准，是遠比 RA 更具即時推進價值的再利用目標。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06957002](https://clinicaltrials.gov/study/NCT06957002) | Phase 2 | 尚未招募 | 40 | 評估 Bosentan 聯合糖皮質激素 vs. 單用糖皮質激素治療**巨細胞動脈炎（GCA）**，主要終點為 12 個月無失敗生存率；試驗目標疾病為 GCA（血管炎性疾病）而非 RA，對 RA 直接證據貢獻極為有限 |

> ⚠️ **注意**：上述試驗針對**巨細胞動脈炎（GCA）**而非類風濕性關節炎，相關性評級為 C（低），不應視為 RA 適應症的直接支持。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [22249931](https://pubmed.ncbi.nlm.nih.gov/22249931/) | 2012 | 動物研究（CIA 模型） | Inflammation Research | Bosentan 在膠原誘導性關節炎小鼠中顯著改善關節炎評分，TNF-α 為驅動 ET 系統基因表達的上游訊號，ERA 在 CIA 具有抗炎效果 |
| [18515326](https://pubmed.ncbi.nlm.nih.gov/18515326/) | 2008 | 動物研究 | Journal of Leukocyte Biology | ET-1 透過 LTB4、TNF-α 及 CXCL-1 調控酵母多糖誘導性關節炎中的嗜中性白血球累積與水腫形成，RA 患者血漿及滑膜 ET-1 升高 |
| [16766656](https://pubmed.ncbi.nlm.nih.gov/16766656/) | 2006 | 動物研究 | PNAS | IL-15 透過 IFN-γ → ET → 前列腺素序列誘導痛覺過敏，雙重 ETA/ETB 拮抗劑可顯著抑制此免疫炎症性痛覺過敏 |
| [19969421](https://pubmed.ncbi.nlm.nih.gov/19969421/) | 2010 | 動物研究 | Pain | IL-17 在抗原誘導性關節炎中介導關節痛覺過敏，ET 訊號為重要下游媒介，與 RA 病理密切相關 |
| [20054770](https://pubmed.ncbi.nlm.nih.gov/20054770/) | 2009 | Case Report | Kardiologia polska | 8.5 歲女童同時診斷 Eisenmenger 症候群及幼年型 RA，以 bosentan 治療心臟病變；確認 ERA 在合併風濕疾病患者的臨床使用可行性 |
| [19851110](https://pubmed.ncbi.nlm.nih.gov/19851110/) | 2010 | Review | Current Opinion in Rheumatology | 皮膚風濕病病理生理學、結果評量及治療進展綜述，涵蓋 ET 訊號在結締組織疾病的作用 |
| [24268012](https://pubmed.ncbi.nlm.nih.gov/24268012/) | 2014 | Review | Rheumatic Diseases Clinics of North America | 結締組織病相關 PAH 的流行病學、預後及治療策略，bosentan 為 CTD-PAH 推薦治療藥物 |

---

## 香港上市資訊

Bosentan 目前在香港**尚無上市許可紀錄**（許可證數：0）。

> 如需參考藥品資訊，可查閱歐盟 EMA 已核准之 Tracleer®（bosentan 62.5mg / 125mg 薄膜衣錠）仿單，核准適應症包含：肺動脈高壓（WHO 功能分級 II-III）及全身性硬化症相關指端潰瘍預防。

---

## 安全性考量

安全性資訊請參考原廠仿單（Tracleer®，Johnson & Johnson / Janssen）。

> 根據已知 bosentan 安全性資料，使用前應特別注意以下事項：
> - **肝毒性**：可見可逆性肝酶（ALT/AST）升高，需定期監測肝功能
> - **致畸胎性**：對孕婦具嚴重致畸風險，育齡女性需嚴格避孕
> - **藥物交互作用**：為 CYP3A4 及 CYP2C9 強誘導劑，與多種藥物（包含 RA 常用之 MTX、cyclosporine）有顯著交互作用風險，用於 RA 患者前需詳細評估合併用藥情形

---

## 結論與下一步

**決策：Hold（研究問題）**

**理由：**
儘管多項動物模型一致顯示 ET-1 訊號在關節炎症中的功能性角色，且 Bosentan 在 CIA 模型中具有抗關節炎效果，目前完全缺乏針對 RA 患者的人體臨床試驗，現有唯一相關試驗（NCT06957002）針對的是機轉差異顯著的 GCA 而非 RA，整體證據等級為 L4（動物/機轉研究）。建議將資源優先投入已有 L1 證據的局限型全身性硬化症（lcSSc）指端潰瘍適應症，待香港上市許可問題解決後再評估 RA 的研究可行性。

**若要推進 RA 適應症研究，需要：**
- 設計 Bosentan 用於 RA 患者的 Phase 1/2 概念驗證（PoC）臨床試驗
- 補充完整 MOA 資料（DrugBank API 查詢，DG002）
- 取得 TFDA/EMA 完整仿單警語及禁忌症，進行正式安全性初評（DG001）
- 評估 RA 常見合併用藥（MTX、生物製劑、NSAIDs）與 Bosentan（CYP3A4/2C9 強誘導劑）之藥物交互作用風險
- **優先建議**：在投入 RA 研究前，先完整評估局限型 SSc（lcSSc）指端潰瘍預防的香港藥品引進可行性（L1 證據，EMA 已核准，推進障礙最低）

---

> ⚠️ **免責聲明**：本報告結果僅供研究參考，不構成醫療建議。老藥新用預測候選需經臨床驗證後方可應用於臨床實踐。資料截止日期：2026-04-05。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

