---
layout: default
title: Cyproterone Acetate
parent: 中證據等級 (L3-L4)
nav_order: 169
evidence_level: L4
indication_count: 10
---

# Cyproterone Acetate
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Cyproterone Acetate：從高雄激素血症到偏頭痛

## 一句話總結

Cyproterone Acetate（CPA）是一種兼具抗雄激素與黃體素雙重活性的化合物，廣泛用於多囊卵巢症候群（PCOS）、多毛症及高雄激素血症的治療。TxGNN 模型預測排名第一的新適應症為**偏頭痛 (migraine disorder)**，目前有 **0 個臨床試驗**和 **3 篇文獻**支持，但現有文獻方向相互矛盾；本次 10 個預測中，**4 個結果（Rank 2、4、6、10）反映的是安全禁忌訊號**而非治療機會，唯一具正向臨床潛力的是排名第八的**閉經 (amenorrhea)**（L3，4 項臨床試驗，14 篇文獻）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高雄激素血症（PCOS、多毛症、荷爾蒙性避孕） |
| 預測新適應症（Rank 1） | 偏頭痛 (migraine disorder) |
| TxGNN 預測分數 | 99.66% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉（MOA）資料。根據已知資訊，CPA 屬 C21 類固醇，可競爭性阻斷雄激素受體，同時抑制促性腺激素（LH/FSH）分泌，在多囊卵巢症候群和多毛症中的療效已獲廣泛臨床驗證。

偏頭痛，尤其是月經性偏頭痛，與雌激素週期性波動密切相關。理論上，CPA 作為黃體素可穩定荷爾蒙環境，降低月經誘發偏頭痛的頻率。PMID 14670648 亦指出 CPA 可增加多巴胺釋放並結合阿片受體，而這兩條神經路徑均與偏頭痛的疼痛傳導機轉相關。

然而，現有證據相互矛盾：PMID 12390622（觀察性研究）顯示不同黃體素製劑對停經後偏頭痛的影響各異，部分製劑甚至加重症狀；PMID 10857213（多中心大型研究，n＝2,506 名患者，7,971 人年追蹤）更明確記錄偏頭痛為 CPA 婦科療法的長期副作用之一。在無直接 RCT 的情況下，因果方向尚未確立，證據強度僅達 L4。

---

## 臨床試驗證據（偏頭痛，Rank 1）

目前無相關臨床試驗登記。

---

## 文獻證據（偏頭痛，Rank 1）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [14670648](https://pubmed.ncbi.nlm.nih.gov/14670648/) | 2003 | 基礎科學/回顧 | Maturitas | CPA 可調節 GABA-A 受體、增加紋狀體多巴胺釋放並結合阿片受體，提供偏頭痛神經機轉假說 |
| [12390622](https://pubmed.ncbi.nlm.nih.gov/12390622/) | 2002 | 觀察性世代 | Headache | 三種口服 HRT 方案對停經後偏頭痛的影響各異，部分黃體素製劑加重發作 |
| [10857213](https://pubmed.ncbi.nlm.nih.gov/10857213/) | 2000 | 回顧性不良事件研究 | Zentralblatt fur Gynakologie | n＝2,506，7,971 人年追蹤：持續低劑量 CPA 雖不增加誘變風險，但偏頭痛已記錄為長期副作用 |

---

## 香港上市資訊

Cyproterone Acetate 目前在香港**未有登記上市**，無任何香港藥物許可證記錄。

---

## ⚠️ 重要安全禁忌警示

> **本次 TxGNN 前 10 名預測中，有 4 個預測反映的是 CPA 的臨床危害訊號，而非治療機會。TxGNN 高分（0.99+）源於知識圖譜中 CPA–荷爾蒙–凝血/偏頭痛節點的密集連結（「KG 鄰近效應」），臨床解讀方向為反適應症。**

| Rank | 疾病 | 訊號類型 | 關鍵依據 |
|------|------|---------|---------|
| 2 | 腦幹型先兆偏頭痛 | 🚫 明確禁忌 | CNGOF 臨床指引（PMID 30389542）列為明確禁忌，含 CPA 荷爾蒙製劑在此族群顯著升高缺血性腦中風風險 |
| 4 | 抗凝血酶缺乏 Type 2 | 🚫 高危警示 | CPA 具促血栓效應（增加凝血酶生成），在遺傳性高血栓傾向患者中疊加靜脈血栓栓塞風險，屬理論高危禁忌 |
| 6 | Factor V 過量合併自發性血栓 | 🚫 明確反適應症 | Case-Control 研究（PMID 29614525）：Factor V Leiden 突變合併含 CPA 複合避孕藥使靜脈血栓風險顯著倍增 |
| 10 | 血栓傾向 | 🚫 強烈逆向安全訊號 | 18 篇文獻一致顯示 CPA 為靜脈血栓栓塞的**獨立風險因子**（增加凝血酶生成、降低蛋白 C/S 活性、增加活化蛋白 C 抗性），而非治療藥物 |

---

## 最具潛力正向預測：閉經（Rank 8，L3，Research Question）

在 10 個預測中，**閉經（amenorrhea）** 是唯一具備直接臨床試驗支持且推薦進入 Research Question 評估的適應症。CPA 透過抗雄激素及抗促性腺激素雙重機制，治療 PCOS 相關繼發性閉經具充分的生物學合理性，含 CPA 複合口服避孕藥（如 Diane-35：EE 35mcg + CPA 2mg）已在多個國家核准用於 PCOS 相關月經不規律。

### 臨床試驗證據（閉經）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01103518](https://clinicaltrials.gov/study/NCT01103518) | Phase IV | 未知 | 100 | 隨機雙盲設計，直接比較兩種 EE+CPA 製劑治療高雄激素性月經不規律（含閉經），Grade A 最高直接相關性 |
| [NCT04831151](https://clinicaltrials.gov/study/NCT04831151) | NA | 未知 | 42 | 含 CPA vs 屈螺酮口服避孕藥於 PCOS 婦女血液代謝指標比較（Grade B） |
| [NCT02744131](https://clinicaltrials.gov/study/NCT02744131) | NA | 未知 | 100 | OCP（含 CPA）vs Metformin 改善印度 PCOS 婦女臨床、荷爾蒙及代謝特徵（Grade B） |
| [NCT02729545](https://clinicaltrials.gov/study/NCT02729545) | Phase 2 | 已完成 | 60 | 針灸 vs Diane-35（CPA/EE）改善 PCOS 卵巢功能 RCT，CPA 作為主動對照臂（Grade C） |

### 文獻證據（閉經，前 10 篇）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [9130733](https://pubmed.ncbi.nlm.nih.gov/9130733/) | 1997 | 對照臨床試驗 | Human Reproduction | GnRH-a + EE-CPA 複合療法 vs 單獨 EE-CPA 治療 PCOS 高雄激素症（n＝12），EE-CPA 組月經改善有效 |
| [2946604](https://pubmed.ncbi.nlm.nih.gov/2946604/) | 1986 | 多中心臨床試驗 | Fertility and Sterility | n＝158，比較低劑量（Diane 2mg）vs 高劑量（Androcur 100mg）CPA 治療嚴重多毛症，月經調節為次要終點 |
| [2528199](https://pubmed.ncbi.nlm.nih.gov/2528199/) | 1989 | 回顧 | Rev Fr Gynecologie | CPA 為最有效抗雄激素，用於痤瘡和多毛症；**指出需合併雌激素以避免閉經副作用** |
| [6232474](https://pubmed.ncbi.nlm.nih.gov/6232474/) | 1984 | 回顧/病例系列 | Obstetrics and Gynecology Annual | 多囊卵巢疾病治療策略綜述，CPA 相關療法記錄 |
| [17162716](https://pubmed.ncbi.nlm.nih.gov/17162716/) | 2006 | 病例系列 | Gynecological Endocrinology | 月經性氣胸：治療性閉經期間（荷爾蒙製劑誘發）無氣胸復發，停藥後復發，支持閉經之治療性應用 |
| [1589384](https://pubmed.ncbi.nlm.nih.gov/1589384/) | 1992 | 病例報告 | Postgraduate Medical Journal | PCOS 合併雙側腎上腺皮質腺瘤患者，使用 CPA + EE 治療繼發性閉經三年，提供長期安全性參考 |
| [2137793](https://pubmed.ncbi.nlm.nih.gov/2137793/) | 1990 | 病例報告 | Fertility and Sterility | 家族性高雄激素血症-胰島素抵抗-黑棘皮症合併閉經：GnRH-a + 抗雄激素治療逆轉多毛及恢復月經 |
| [35592826](https://pubmed.ncbi.nlm.nih.gov/35592826/) | 2022 | 病例報告 | Annals of Medicine and Surgery | 先天性腎上腺增生（21-羥化酶缺乏）青少年病例：雄激素過多引起閉經，CPA 類製劑列入治療選項 |
| [23221134](https://pubmed.ncbi.nlm.nih.gov/23221134/) | 2012 | 前瞻性研究 | Georgian Medical News | n＝159，中樞性月經障礙不孕婦女，以腦電圖指導荷爾蒙療法（含 CPA 類製劑）改善寡/閉經 |
| [12266391](https://pubmed.ncbi.nlm.nih.gov/12266391/) | 1984 | 回顧 | J Bras Ginecologia | CPA 作為新型排卵抑制抗雄激素製劑的臨床應用綜述 |

---

## 10 個預測適應症完整總覽

| Rank | 疾病 | TxGNN 分數 | 證據等級 | 建議 | 主要備註 |
|------|------|-----------|---------|------|---------|
| 1 | migraine disorder | 99.66% | L4 | Hold | 機轉假說存在，但文獻顯示 CPA 可能誘發/加重偏頭痛，方向矛盾 |
| 2 | migraine with brainstem aura | 99.58% | L5 | Hold | 🚫 CNGOF 指引明確禁忌，升高缺血性腦血管意外風險 |
| 3 | Prinzmetal angina | 99.52% | L5 | Hold | 無已知機轉連結，無文獻，純 KG 網絡鄰近效應 |
| 4 | antithrombin deficiency type 2 | 99.48% | L5 | Hold | 🚫 CPA 促血栓效應在高血栓傾向患者疊加風險，理論高危禁忌 |
| 5 | heparin cofactor 2 deficiency | 99.45% | L5 | Hold | 極罕見疾病，無任何臨床或基礎科學佐證 |
| 6 | factor 5 excess w/ thrombosis | 99.45% | L5 | Hold | 🚫 Factor V Leiden + CPA 靜脈血栓風險倍增（PMID 29614525），明確反適應症 |
| 7 | migraine w/ or w/o aura susceptibility | 99.34% | L4 | Hold | 遺傳易感性分類非治療標的；20 篇文獻多屬癲癇遺傳學，與 CPA 無直接關聯 |
| **8** | **amenorrhea (disease)** | **99.28%** | **L3** | **Research Question** | ✅ 最具潛力：4 項臨床試驗（含 Phase IV）+ 直接機轉連結 |
| 9 | breast fibrocystic disease | 99.15% | L4 | Hold | 觀察性 HRT 及跨性別族群研究，無直接 CPA 介入設計，外推性受限 |
| 10 | thrombophilia | 99.03% | L4 | Hold | 🚫 18 篇文獻一致顯示 CPA 為靜脈血栓栓塞的風險因子而非治療藥物 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

根據本評估收集的文獻，以下安全性訊號需特別重視：

- **靜脈血栓栓塞風險**：多項研究記錄 CPA 可增加凝血酶生成（PMID 18064335，機轉 RCT 設計）、降低蛋白 S 活性（PMID 15550051，世代研究）及增加活化蛋白 C 抗性（PMID 24438944，世代研究），顯著升高靜脈血栓栓塞（VTE）風險
- **腦幹型先兆偏頭痛禁忌**：含 CPA 荷爾蒙製劑在此族群屬法國 CNGOF 指引明確禁忌（PMID 30389542）
- **遺傳性凝血異常協同效應**：Factor V Leiden 突變攜帶者合併使用含 CPA 複合避孕藥，靜脈血栓風險協同倍增（PMID 29614525、PMID 32342502）
- **跨性別族群特殊考量**：男性至女性跨性別者使用 CPA 合併雌激素期間，靜脈血栓風險視雌激素給藥途徑而異（PMID 14671159）

---

## 結論與下一步

### 主要預測（Rank 1：偏頭痛）

**決策：Hold**

**理由：**
3 篇文獻提供相互矛盾的機轉依據，無直接臨床試驗；PMID 10857213 大型多中心研究已記錄偏頭痛為 CPA 長期副作用之一，因果方向不明確，整體證據不支持推進。

**若要推進需要：**
- 補充 CPA 完整作用機轉（MOA）資料（DrugBank API 查詢）
- 香港 TFDA 仿單警語與禁忌全文解析
- 釐清偏頭痛誘發 vs 預防的因果方向，設計以月經性偏頭痛亞型為主要終點的前瞻性研究

---

### 優先推進目標（Rank 8：閉經）

**決策：Proceed with Guardrails（進入 S2 評估）**

**理由：**
CPA 抗雄激素/抗促性腺激素機轉治療 PCOS 相關繼發性閉經具充分生物學合理性；含 CPA 複合口服避孕藥（Diane-35）已在多個國家（包括香港周邊地區）核准用於 PCOS 相關月經不規律，Phase IV 直接試驗設計（NCT01103518）提供初步臨床依據。

**若要推進需要：**
- 評估向香港衞生署（Department of Health）申請藥物登記的可行性
- 設計以「閉經恢復率」為主要終點的專項臨床試驗方案
- 建立嚴格血栓高危族群排除標準（Factor V Leiden、抗凝血酶缺乏、個人/家族 VTE 病史）
- 補充 CPA 單藥（Androcur 系列）vs 複合製劑（Diane-35）的療效與安全性比較數據

---

> ⚠️ **免責聲明**：本報告結果僅供研究參考，不構成醫療建議。所有老藥新用候選需經過臨床驗證才能應用於實際醫療決策。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

