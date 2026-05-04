---
layout: default
title: Adefovir Dipivoxil
parent: 僅模型預測 (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
---

# Adefovir Dipivoxil
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

# Adefovir Dipivoxil：從慢性乙型肝炎到慢性丙型肝炎病毒感染

## 一句話總結

Adefovir Dipivoxil 是一種核苷酸類似物（acyclic nucleoside phosphonate），FDA 核准用於治療慢性乙型肝炎（HBV），品牌名 Hepsera；目前香港未上市。
TxGNN 模型預測它可能對**慢性丙型肝炎病毒感染 (Chronic Hepatitis C Virus Infection)** 有效，預測分數高達 **99.97%**；
然而深入分析後，此為**知識圖譜偽陽性預測**——蒐集到的 9 個臨床試驗均屬 HBV 研究，且 Adefovir 的 DNA 聚合酶靶標與 HCV 的 RNA 複製機轉根本不符。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性乙型肝炎病毒感染（HBV，FDA 核准；HK 未上市） |
| 預測新適應症 | 慢性丙型肝炎病毒感染 (Chronic HCV Infection) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L4（機轉不符，無直接 HCV 研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Adefovir Dipivoxil 的活性代謝物 adefovir diphosphate 作為 dATP 的競爭性類似物，進入細胞後透過以下機轉抑制 HBV 複製：

1. 競爭性抑制 HBV DNA 聚合酶（具逆轉錄酶活性），干擾病毒前基因組 RNA 反轉為 DNA
2. 整合進病毒 DNA 後導致鏈終止
3. 對野生型及拉米夫定耐藥株（YMDD 變異）均有效

**⚠️ 機轉分析：此 HCV 預測在生物學上不成立。** HCV 是正鏈 RNA 病毒（Flaviviridae 科），複製完全依賴 NS5B RNA 依賴性 RNA 聚合酶（RdRp），整個複製週期**不存在任何 DNA 中間體或逆轉錄步驟**。Adefovir 的作用靶點（HBV DNA 聚合酶）在 HCV 感染週期中完全缺席，理論上對 NS5B 無任何抑制活性。

TxGNN 預測分數 0.9997 極可能源於知識圖譜中 HBV 與 HCV 共享「慢性病毒性肝炎（chronic viral hepatitis）」超類節點，造成基於圖譜節點距離近似的偽陽性關聯，而非真實的藥物–疾病交互作用信號。

---

## 臨床試驗證據

> ⚠️ **重要說明：** 以下所有試驗均為 HBV 相關研究（或已撤回試驗），**無任何直接針對 HCV 的 Adefovir Dipivoxil 臨床試驗登記**。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00371761](https://clinicaltrials.gov/study/NCT00371761) | Phase 3 | 完成 | 25 | 台灣 HBeAg 陽性慢性 HBV 比較研究（PegIntron vs Adefovir），為 HBV 試驗，非 HCV |
| [NCT00013702](https://clinicaltrials.gov/study/NCT00013702) | Phase 2 | 完成 | 30 | HIV 合併 HBV 肝硬化患者加用 Adefovir 療效與安全性評估，非 HCV |
| [NCT00275938](https://clinicaltrials.gov/study/NCT00275938) | Phase 2/3 | 完成 | 120 | 干擾素 α2b + 利巴韋林治療慢性 HBV 肝炎，Adefovir 非主要研究藥物 |
| [NCT00051077](https://clinicaltrials.gov/study/NCT00051077) | Phase 2 | 撤回 | 0 | HBV/HCV/HIV 三重感染研究，已撤回且 n=0，無任何有效數據 |
| [NCT01205165](https://clinicaltrials.gov/study/NCT01205165) | Phase 4 | 完成 | 104 | 韓國 CHB 患者 Adefovir 抗病毒效果 52 週評估，非 HCV |
| [NCT00645294](https://clinicaltrials.gov/study/NCT00645294) | Phase 1/2 | 完成 | 47 | 兒童及青少年慢性 HBV 感染者 Adefovir 單劑藥動學研究，無 HCV 療效評估 |
| [NCT01925820](https://clinicaltrials.gov/study/NCT01925820) | Phase 4 | 未知 | 540 | HBeAg 陰性 CHB：Pegasys + Entecavir 三臂比較，ADV 僅列於背景藥物清單 |

---

## 文獻證據

以下文獻均涉及 HBV 治療或病毒性肝炎通論，無 Adefovir 直接治療 HCV 的療效報告：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [25892855](https://pubmed.ncbi.nlm.nih.gov/25892855/) | 2015 | Observational | Mediators Inflamm | 慢性 HBV/HCV 患者抗病毒治療前後循環 B 細胞 TLR-9、CD86、CD95 表型差異，HCV 為背景病例 |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | HBV/HCV 抗病毒藥物（含 adefovir dipivoxil）對腎功能影響的綜述，討論腎毒性風險 |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | 慢性 B/C 型肝炎現有治療與未來展望，以 HBV 治療策略（pegIFN、lamivudine、adefovir）為核心 |
| [19149648](https://pubmed.ncbi.nlm.nih.gov/19149648/) | 2009 | Review | Med Chem | Bicyclol 新型抗 HBV/HCV 藥物研究，Adefovir 僅為背景比較藥物 |
| [22370225](https://pubmed.ncbi.nlm.nih.gov/22370225/) | 2012 | Guideline | Orvosi Hetilap | 匈牙利 B/C/D 型病毒性肝炎診療共識指引（2012 年版），含 Adefovir HBV 治療建議 |
| [16880074](https://pubmed.ncbi.nlm.nih.gov/16880074/) | 2006 | Review | Gastroenterol Clin North Am | HBV 感染治療路徑，Adefovir 作為核苷酸類似物的臨床地位討論 |
| [15588803](https://pubmed.ncbi.nlm.nih.gov/15588803/) | 2004 | Review | Best Pract Res Clin Gastroenterol | 慢性病毒性肝炎治療策略，涵蓋 HBV（干擾素、lamivudine、adefovir）與 HCV（IFN+RBV）並行討論 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
Adefovir Dipivoxil 靶向 HBV DNA 聚合酶，而 HCV 複製機轉完全依賴 NS5B RNA 依賴性 RNA 聚合酶，兩者無任何共同靶點。TxGNN 的 99.97% 高分預測係知識圖譜節點共享所致的偽陽性，所有蒐集到的「相關」試驗均屬 HBV 研究。此外，現代直接抗病毒藥物（DAA，如 Sofosbuvir/Velpatasvir 複方）治療 HCV 基因型 1–6 型已達 >95% SVR12，此方向完全無再利用研究價值。

**若要推進需要：**

此方向**不建議推進**（機轉根本不符，且已有高效 HCV 特異性療法）。

建議將 Adefovir Dipivoxil 的後續評估重點轉向以下兩個方向：

1. **B 型肝炎病毒感染（Rank 6，TxGNN 99.87%，L1 證據，Proceed with Guardrails）**
   - FDA 核准適應症（Hepsera），多項已完成 Phase 3 RCT 支持療效（如 NCT00116805、NCT01300234、NCT00857675）
   - 需評估香港上市可行性及正式申請許可證流程
   - 長期用藥（>5 年）需定期監測 eGFR 及血清磷，預防 Fanconi syndrome
   - 注意：現行 AASLD/EASL 指引已將 TDF/TAF 列為一線，Adefovir 多用於特定二線或過渡情境

2. **HIV 感染（Rank 2，TxGNN 99.95%，L1 證據，Hold）**
   - 藥物最初即針對 HIV 開發；Phase 3 RCT（NCT00001082，n=505）已完成，具最高級別直接臨床證據
   - 因所需治療劑量（120 mg/day）遠高於 HBV 劑量（10 mg/day），腎毒性（Fanconi syndrome）為劑量限制性毒性
   - Tenofovir（TDF/TAF）在安全性與療效上已完全取代，此方向**無再利用可行性**

> ⚠️ **本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證方可應用。**
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

